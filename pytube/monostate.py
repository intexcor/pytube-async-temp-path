# -*- coding: utf-8 -*-
from typing import Any, Awaitable, Callable, Optional


class Monostate:
    def __init__(
        self,
        on_progress: Optional[Callable[[Any, bytes, int], Awaitable[None]]],
        on_complete: Optional[Callable[[Any, Optional[str]], Awaitable[None]]],
        title: Optional[str] = None,
        duration: Optional[int] = None,
    ):
        self.on_progress = on_progress
        self.on_complete = on_complete
        self.title = title
        self.duration = duration
