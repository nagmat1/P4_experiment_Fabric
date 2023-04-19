try:
    slice = fablib.get_slice(name=slice_name)

    slice.delete()
except Exception as e:
    print(f"Exception: {e}")
