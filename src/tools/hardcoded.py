import re

from langchain_core.tools import tool

pattern = re.compile(r"""
    ^\s*
    (                           # Start group
        washington              # "Washington"
        (?:\s*,?\s*             # optional space/comma
            d\.?c\.?            # DC, D.C., D C, etc.
        )?                      # DC is optional
      |                         # OR
        d\.?c\.?                # DC alone
    )
    \.?                         # optional trailing period
    \s*$
""", re.IGNORECASE | re.VERBOSE)


def is_washington_dc(city: str) -> bool:
    return pattern.match(city) is not None


@tool(
    "get_weather",
    description="Get the weather for a given city")
def get_weather(city: str) -> str:
    if city == "San Francisco":
        return "It's sunny in San Francisco."
    if city == "Seattle":
        return "It's rainy in Seattle."
    if city == "New York":
        return "It's cloudy in New York."
    if city == "Los Angeles":
        return "It's warm and sunny in Los Angeles."
    if city == "Chicago":
        return "It's windy in Chicago."
    if city == "Miami":
        return "It's hot and humid in Miami."
    if city == "Denver":
        return "It's clear and cool in Denver."
    if city == "Boston":
        return "It's snowy in Boston."
    if is_washington_dc(city):
        return "It's trumpy in Washington D.C."

    return f"It's always sunny in {city}!"
