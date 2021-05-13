from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        del bag[item_id]
        if not bag[item_id]:
            bag.pop(item_id)
        else:
            if quantity > 0:
                bag[item_id] = quantity
            else:
                bag.pop(item_id)

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = None
        if 'product' in request.POST:
            product = request.POST['product']
        bag = request.session.get('bag', {})

        if product:
            del bag[item_id]
            if not bag[item_id]:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
