from django.shortcuts import render, redirect


def view_bag(request):
    """" A view to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """" Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    reddirect_url = request.POST.get('redirect_url')

    # get that bag from the session if exist
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(reddirect_url)
