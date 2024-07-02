import ctypes

# Get the scaling factor
def get_scaling_factor():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()  # Optional, makes the app DPI aware to get accurate scaling
    # Get the scaling factor
    return user32.GetSystemMetrics(0) / user32.GetSystemMetrics(78), user32.GetSystemMetrics(1) / user32.GetSystemMetrics(79)

scaling_factor_x, scaling_factor_y = get_scaling_factor()
print(f"Scaling Factor X: {scaling_factor_x}, Scaling Factor Y: {scaling_factor_y}")
