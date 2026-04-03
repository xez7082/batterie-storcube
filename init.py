from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up StorCube from config entry."""

    hass.data.setdefault(DOMAIN, {})

    # exemple coordinator déjà créé ailleurs
    coordinator = await create_coordinator(hass, entry)

    hass.data[DOMAIN][entry.entry_id] = {
        "coordinator": coordinator,
    }

    await hass.config_entries.async_forward_entry_setups(
        entry, ["sensor"]
    )

    return True
