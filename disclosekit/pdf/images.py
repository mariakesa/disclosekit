# disclosekit/pdf/images.py

def page_has_images(page) -> bool:
    """
    Detect whether a PDF page contains image XObjects.

    Returns True if at least one image is present.
    """
    try:
        resources = page.get("/Resources")
        if resources is None:
            return False

        xobject = resources.get("/XObject")
        if xobject is None:
            return False

        for obj in xobject.values():
            try:
                subtype = obj.get("/Subtype")
                if subtype == "/Image":
                    return True
            except Exception:
                # Ignore malformed objects
                continue

        return False
    except Exception:
        # Fail closed: assume no images if inspection fails
        return False
