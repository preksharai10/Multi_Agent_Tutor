PHYSICS_CONSTANTS = {
    "speed of light": "299,792,458 m/s",
    "gravitational constant": "6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻²",
    "planck constant": "6.62607015 × 10⁻³⁴ J s",
    "electron mass": "9.10938356 × 10⁻³¹ kg",
    "proton mass": "1.6726219 × 10⁻²⁷ kg"
}

def lookup_constant(name: str) -> str:
    key = name.strip().lower()
    return PHYSICS_CONSTANTS.get(key, f"Constant '{name}' not found.")
