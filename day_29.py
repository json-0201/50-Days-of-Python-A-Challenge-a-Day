# Middle Figure

def middle_figure(a: str, b: str) -> str:
    """Combines two strings and returns the middle element."""

    text = (a+b).replace(" ","")
    
    return text[int(len(text)/2)] if len(text) % 2 == 1 else "no middle figure"

print(middle_figure("make love", "not wars"))
