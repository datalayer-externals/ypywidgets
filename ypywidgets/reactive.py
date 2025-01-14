from __future__ import annotations
from typing import Callable

from reacttrs.reactive import Reactive, ReactiveType


def set_attr(obj, name, value):
    try:
        obj._attrs[name] = value
    except RuntimeError:
        # Already mutably borrowed
        pass


class reactive(Reactive[ReactiveType]):
    def __init__(
        self,
        default: ReactiveType | Callable[[], ReactiveType],
        *,
        init: bool = True,
        always_update: bool = False,
        sync: bool = True,
    ) -> None:
        on_set = set_attr if sync else None
        super().__init__(
            default,
            init=init,
            always_update=always_update,
            on_set=on_set,
        )
