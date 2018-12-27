function dimension_to_num(dimension_str)
{
    if (dimension_str.includes("px"))
        return Number(dimension_str.replace("px", ""));
    return -1;
}

function get_css(elem, property)
{
    return window.getComputedStyle(elem, null).getPropertyValue(property);
}

function get_relative_parent(element)
{
    let curr = element;
    while (curr.parentElement &&
           get_css(curr.parentElement, "position") !== "relative")
        curr = curr.parentElement;
    return curr.parentElement;
}
