#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# Adapted from https://github.com/tornadoweb/tornado/blob/master/demos/blog/blog.py

import aiosqlite
import os.path
import re
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("db_file", default="widgets.db", help="sqlite database file")


class Application(tornado.web.Application):
    def __init__(self, db):
        self.db = db
        handlers = [
            (r"/", HomeHandler),
        ]

        settings = dict(
            site_title="The Widget Website",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Widget": WidgetModule},
            cookie_secret="__NOT_A_GOOD_SECRET__",
            xsrf_cookies=True,
            debug=True,
        )

        super().__init__(handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):
    def row_to_obj(self, row, cur):
        """Convert a SQL row to an object supporting dict and attribute access."""
        obj = tornado.util.ObjectDict()
        for val, desc in zip(row, cur.description):
            obj[desc[0]] = val # for aiosqlite this returns a tuple
        return obj

    async def execute(self, stmt, *args):
        """Execute a SQL statement.
        Must be called with ``await self.execute(...)``
        """
        with (await self.application.db.cursor()) as cur:
            await cur.execute(stmt, args)

    async def query(self, stmt, *args):
        """Query for a list of results.
        Typical usage::
            results = await self.query(...)
        Or::
            for row in await self.query(...)
        """

        async with self.application.db.execute(stmt, args) as cur:
            return [self.row_to_obj(row, cur) for row in await cur.fetchall()]

    async def queryone(self, stmt, *args):
        """Query for exactly one result.
        Raises NoResultError if there are no results, or ValueError if
        there are more than one.
        """
        results = await self.query(stmt, *args)
        if len(results) == 0:
            raise NoResultError()
        elif len(results) > 1:
            raise ValueError("Expected 1 result, got %d" % len(results))
        return results[0]


class HomeHandler(BaseHandler):
    async def get(self):
        widgets = await self.query(
            """
            SELECT
                widget_id,
                code,
                name,
                num_parts,
                created_at,
                updated_at
            FROM
                WIDGET
            ORDER BY
                updated_at DESC,
                created_at DESC
            LIMIT 5
            """
        )
        self.render("home.html", widgets=widgets)

class WidgetModule(tornado.web.UIModule):
    def render(self, widget):
        return self.render_string("modules/widget.html", widget=widget)


async def main():
    tornado.options.parse_command_line()

    async with aiosqlite.connect(
            options.db_file,
    ) as db:
        db.row_factory = aiosqlite.Row
        app = Application(db)
        app.listen(options.port)

        # Shutdown with Ctrl-c
        shutdown_event = tornado.locks.Event()
        await shutdown_event.wait()


if __name__ =="__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
