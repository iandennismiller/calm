import os
import psutil


def get_ram():
    ram = psutil.virtual_memory().total
    for steps in [196, 128, 64, 32, 16, 8]:
        if ram / 1e9 >= steps:
            return steps

def get_resource_max(num_parameters):
    """
    Based on amount of physical RAM and a number of parameters, estimate the optimal quant and maximum possible context size
    """
    ram = get_ram()

    if num_parameters == "180b":
        if ram == 196:
            return {"quant": "Q4_K_S", "context_size": 1024}
    elif num_parameters == "70b":
        if ram == 196:
            return {"quant": "f16", "context_size": 8192}
        elif ram == 128:
            return {"quant": "Q6_K", "context_size": 4096}
        elif ram == 64:
            return {"quant": "Q4_K_S", "context_size": 2048}
    elif num_parameters in ["33b", "30b"]:
        if ram >= 64:
            return {"quant": "f16", "context_size": 8192}
        elif ram == 64:
            return {"quant": "Q6_K", "context_size": 8192}
        elif ram == 32:
            return {"quant": "Q4_K_S", "context_size": 2048}
    elif num_parameters == "13b":
        if ram >= 64:
            return {"quant": "f16", "context_size": 8192}
        elif ram == 32:
            return {"quant": "Q6_K", "context_size": 8192}
        elif ram == 16:
            return {"quant": "Q4_K_S", "context_size": 2048}
    elif num_parameters == "7b":
        if ram >= 32:
            return {"quant": "f16", "context_size": 4096}
        elif ram == 16:
            return {"quant": "Q6_K", "context_size": 8192}
        elif ram == 8:
            return {"quant": "Q4_K_S", "context_size": 2048}
    elif num_parameters == "3b":
        if ram >= 16:
            return {"quant": "f16", "context_size": 8192}
        elif ram == 8:
            return {"quant": "Q6_K", "context_size": 4096}
        elif ram == 4:
            return {"quant": "Q4_K_S", "context_size": 2048}
    elif num_parameters == "1b":
        if ram >= 4:
            return {"quant": "Q6_K", "context_size": 8192}
        elif ram == 2:
            return {"quant": "Q4_K_S", "context_size": 2048}

def has_metal():
    basepath = "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer"
    macossdk = os.path.join(basepath, "SDKs", "MacOSX.sdk")
    name = "Metal"

    p = os.path.join(macossdk, "System", "Library", "Frameworks", name + ".framework")
    return os.path.isdir(p)

def get_cores():
    # return the number of cores this CPU has
    return psutil.cpu_count(logical=False)
