from typing import TYPE_CHECKING

from aiohttp import ClientSession

from reverse_image_search.providers.base import Provider
from reverse_image_search.providers.booru import BooruProvider

if TYPE_CHECKING:
    from reverse_image_search.app import ReverseImageSearch


async def initiate_data_providers(
    session: ClientSession, config: "ReverseImageSearch.Arguments"
) -> dict[str, Provider]:
    return {
        "booru": BooruProvider(session, config.boorus),
    }