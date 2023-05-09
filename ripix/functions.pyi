from asyncio import AbstractEventLoop
from typing import TypeVar, Iterable, AsyncGenerator, overload, SupportsIndex, Callable, Optional, Any, Coroutine

T = TypeVar("T")


async def aiter(it: Iterable[T]) -> AsyncGenerator[T]: ...

@overload
async def arange(__stop: SupportsIndex) -> AsyncGenerator[int]: ...
@overload
async def arange(__start: SupportsIndex, __stop: SupportsIndex, __step: SupportsIndex=...) -> AsyncGenerator[int]: ...

async def run_in_executor(loop: Optional[AbstractEventLoop], executor: Optional[Any], func: Callable[..., T], *args, **kwargs) -> T: ...

def wrapper_run_in_executor(loop: Optional[AbstractEventLoop], executor, func: Callable[..., T]) -> Callable[..., Coroutine[Any, Any, T]]: ...