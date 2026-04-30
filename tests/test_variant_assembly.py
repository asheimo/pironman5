"""Tests for the modular variant assembly system."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_products_assemble_without_error():
    """Every product definition should assemble without errors."""
    from pironman5.variants.products import PRODUCT_DEFINITIONS
    from pironman5.variants.modules import assemble

    for key, product in PRODUCT_DEFINITIONS.items():
        result = assemble(product["modules"])
        assert isinstance(result["peripherals"], list)
        assert isinstance(result["default_config"], dict)
        assert isinstance(result["event_map"], dict)
        assert len(result["peripherals"]) > 0
        print(f"  {key}: {len(result['peripherals'])} peripherals, {len(result['default_config'])} config keys")


def test_dependency_resolution():
    from pironman5.variants.modules import resolve_dependencies

    # gpio_fan_led depends on gpio_fan
    resolved = resolve_dependencies(["gpio_fan_led"])
    assert "gpio_fan" in resolved
    assert "gpio_fan_led" in resolved
    assert resolved.index("gpio_fan") < resolved.index("gpio_fan_led")
    print("Dependency resolution: OK")


def test_custom_peripheral():
    from pironman5.variants.modules import assemble

    # Custom list with core + oled only
    result = assemble(["core", "oled"])
    assert "storage" in result["peripherals"]
    assert "oled" in result["peripherals"]
    assert "ws2812" not in result["peripherals"]
    assert "history" not in result["peripherals"]

    # Custom list with pipower5
    result = assemble(["core", "pipower5"])
    assert "pipower5" in result["peripherals"]
    assert "shutdown_percentage" in result["default_config"]
    assert "oled" not in result["peripherals"]
    print("Custom peripheral assembly: OK")


def test_unknown_module():
    from pironman5.variants.modules import get

    try:
        get("nonexistent")
        assert False, "Should have raised KeyError"
    except KeyError as e:
        assert "nonexistent" in str(e)
    print("Unknown module error: OK")


def test_duplicate_module_names():
    from pironman5.variants.modules import assemble

    result = assemble(["core", "core", "core"])
    # Should deduplicate -> no duplicate peripherals
    assert result["peripherals"].count("storage") == 1
    print("Duplicate module dedup: OK")


def test_empty_module_list():
    from pironman5.variants.modules import assemble

    result = assemble([])
    assert result["peripherals"] == []
    assert result["default_config"] == {}
    assert result["event_map"] == {}
    print("Empty module list: OK")


def test_variant_imports():
    from pironman5.variants import NAME, ID, PRODUCT_VERSION, PERIPHERALS, SYSTEM_DEFAULT_CONFIG, EVENT_MAP, DT_OVERLAYS, VARIENT
    assert isinstance(NAME, str)
    assert isinstance(ID, str)
    assert isinstance(PERIPHERALS, list)
    assert isinstance(SYSTEM_DEFAULT_CONFIG, dict)
    assert isinstance(EVENT_MAP, dict)
    assert isinstance(DT_OVERLAYS, list)
    assert isinstance(VARIENT, str)
    print(f"Variant imports OK: NAME={NAME}, ID={ID}, peripherals={len(PERIPHERALS)}")


if __name__ == "__main__":
    test_products_assemble_without_error()
    test_dependency_resolution()
    test_custom_peripheral()
    test_unknown_module()
    test_duplicate_module_names()
    test_empty_module_list()
    test_variant_imports()
    print("\nAll tests passed.")
