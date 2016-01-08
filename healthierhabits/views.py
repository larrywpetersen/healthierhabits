from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Groups, Rewards, Customers, Orders


class Link( ):
    file = 'file'
    name = 'name'
    def __init__( self, file, name):
        self.file = file
        self.name = name



def index( request):
    context = {}
    return render( request, 'healthierhabits/home.html', context)


def groups_home(request):
    subgroup = 'Groups'
    all_links = []
    all_links.extend( [  Link( 'add', 'Add a Group' ) ] )
    all_links.extend( [ Link( 'list', 'List of Groups') ] )
    all_links.extend( [ Link( 'csv', 'List of Groups (csv format)') ] )
    context = {}
    context[ 'subgroup'
    ] = subgroup
    context[ 'all_links' ] = all_links
    return render( request, 'healthierhabits/common/home.html', context)


def groups_add( request):
    context = {}
    return render( request, 'healthierhabits/groups/add.html', context)


def groups_add_action( request):
    group = Groups()
    group.name = request.POST[ 'name']
    group.address1 = request.POST[ 'address1']
    group.address2 = request.POST[ 'address2']
    group.city = request.POST[ 'city']
    group.state = request.POST[ 'state']
    group.zip = request.POST[ 'zip']
    group.email = request.POST[ 'email']
    group.phone = request.POST[ 'phone']
    group.save()
    context = { 'new_group' : [ group] }
    return render( request, 'healthierhabits/groups/add_confirm.html', context)


def groups_list(request):
    subgroup = 'Groups'
    all_rows = Groups.objects.order_by( 'name')
    context = {}
    context[ 'subgroup' ] = subgroup
    context[ 'all_rows' ] = all_rows
    return render( request, 'healthierhabits/common/list.html', context)


def groups_detail( request, groupid):
    group = Groups.objects.get( id=groupid)
    context = {}
    context[ 'group'] = group
    return render( request, 'healthierhabits/groups/detail.html', context)


def groups_edit( request, groupid):
    group = Groups.objects.get( id=groupid)
    context = {}
    context[ 'group'] = group
    return render( request, 'healthierhabits/groups/edit.html', context)


def groups_edit_action( request):
    groupid = request.POST[ 'id' ]
    group = Groups.objects.get( id=groupid)
    group.name = request.POST[ 'name']
    group.address1 = request.POST[ 'address1']
    group.address2 = request.POST[ 'address2']
    group.city = request.POST[ 'city']
    group.state = request.POST[ 'state']
    group.zip = request.POST[ 'zip']
    group.email = request.POST[ 'email']
    group.phone = request.POST[ 'phone']
    group.save()
    context = { 'new_group' : [ group] }
    return render( request, 'healthierhabits/groups/edit_confirm.html', context)


def groups_csv( request):
    groups = Groups.objects.all()
    msg = 'Group ID, Name, Address1, Address2, City, State, Zip, email, '
    msg = msg + 'phone<br>'   # Windows wants cr lf
    for g in groups:
        msg = msg + str( g.id) + ', ' + g.name + ', ' + g.address1 + ', '
        msg = msg + g.address2 + ', ' + g.city + ', ' + g.state + ', '
        msg = msg + g.zip + ', ' + g.email + ', ' + g.phone + '<br>'
    return HttpResponse( msg)





def rewards_home(request):
    subgroup = 'Rewards'
    all_links = []
    all_links.extend( [  Link( 'add', 'Add a Reward' ) ] )
    all_links.extend( [ Link( 'list', 'List of Rewards') ] )
    all_links.extend( [ Link( 'csv', 'List of Rewards (csv format)') ] )
    context = { 'subgroup' : subgroup }
    context[ 'all_links' ]= all_links
    return render( request, 'healthierhabits/common/home.html', context)


def rewards_add( request):
    all_groups = Groups.objects.all()
    context = { 'all_groups' : all_groups }
    return render( request, 'healthierhabits/rewards/add.html', context)


def rewards_add_action( request):
    reward = Rewards()
    reward.group = Groups.objects.get( id = request.POST[ 'group'])
    reward.name = request.POST[ 'name']
    reward.price = request.POST[ 'price']
    reward.available = request.POST[ 'available']
    reward.number_given = request.POST[ 'number_given']
    reward.save()
    context = { 'new_reward' : [ reward] }
    return render( request, 'healthierhabits/rewards/add_confirm.html', context)


def rewards_list(request):
    subgroup = 'Rewards'
    all_rows = Rewards.objects.order_by( 'group__name')
    context = {}
    context[ 'subgroup' ] = subgroup
    context[ 'all_rows' ] = all_rows
    return render( request, 'healthierhabits/common/list.html', context)


def rewards_detail( request, rewardid):
    reward = Rewards.objects.get( id=rewardid)
    context = {}
    context[ 'reward'] = reward
    return render( request, 'healthierhabits/rewards/detail.html', context)


def rewards_edit( request, rewardid):
    reward = Rewards.objects.get( id=rewardid)
    all_groups = Groups.objects.all()
    context = {}
    context[ 'reward'] = reward
    context[ 'all_groups'] = all_groups
    return render( request, 'healthierhabits/rewards/edit.html', context)


def rewards_edit_action( request):
    rewardid = request.POST[ 'id' ]
    reward = Rewards.objects.get( id=rewardid)
    reward.group = Groups.objects.get( id = request.POST[ 'group'])
    reward.name = request.POST[ 'name']
    reward.price = request.POST[ 'price']
    if( request.POST[ 'available' ] == 'Yes'):
        reward.available = True
    else:
        reward.available = False
    reward.number_given = request.POST[ 'number_given']
    reward.save()
    context = { 'new_reward' : [ reward] }
    return render( request, 'healthierhabits/rewards/edit_confirm.html', context)


def rewards_csv( request):
    rewards = Rewards.objects.all()
    msg = 'Reward ID, Group ID, Group, Name, Price, Available, '
    msg = msg + 'Number Given<br>'   # Windows wants cr lf
    for r in rewards:
        msg = msg + str( r.id) + ', ' + str( r.group.id) + ', '
        msg = msg + r.group.name_string() + ', '
        msg = msg + r.name_string() + ', ' + str( r.price) + ', '
        msg = msg + r.available_yn() + ', ' + str( r.number_given) + '<br>'
    return HttpResponse( msg)





def customers_home(request):
    subgroup = 'Customers'
    all_links = []
    all_links.extend( [  Link( 'add', 'Add a Customer' ) ] )
    all_links.extend( [ Link( 'list', 'List of Customers') ] )
    all_links.extend( [ Link( 'csv', 'List of Customers (csv format)') ] )
    context = {}
    context[ 'subgroup' ] = subgroup
    context[ 'all_links' ]= all_links
    return render( request, 'healthierhabits/common/home.html', context)


def customers_add( request):
    all_groups = Groups.objects.all()
    context = {}
    context[ 'all_groups' ]= all_groups
    return render( request, 'healthierhabits/customers/add.html', context)


def customers_add_action( request):
    customer = Customers()
    customer.firstname = request.POST[ 'firstname']
    customer.lastname = request.POST[ 'lastname']
    customer.address1 = request.POST[ 'address1']
    customer.address2 = request.POST[ 'address2']
    customer.city = request.POST[ 'city']
    customer.state = request.POST[ 'state']
    customer.zip = request.POST[ 'zip']
    customer.email1 = request.POST[ 'email1']
    customer.email2 = request.POST[ 'email2']
    customer.phone1 = request.POST[ 'phone1']
    customer.phone1 = request.POST[ 'phone2']
    customer.group = Groups.objects.get( id = request.POST[ 'group'] )
    customer.current_points = request.POST[ 'current_points']
    customer.life_points = request.POST[ 'life_points']
    customer.save()
    context = { 'new_customer' : [ customer] }
    return render( request, 'healthierhabits/customers/add_confirm.html', context)


def customers_list(request):
    subgroup = 'Customers'
    all_rows = Customers.objects.order_by( 'lastname', 'firstname')
    context = {}
    context[ 'subgroup' ] = subgroup
    context[ 'all_rows' ] = all_rows
    return render( request, 'healthierhabits/common/list.html', context)


def customers_detail( request, customerid):
    customer = Customers.objects.get( id=customerid)
    context = {}
    context[ 'customer'] = customer
    return render( request, 'healthierhabits/customers/detail.html', context)


def customers_csv( request):
    customers = Customers.objects.all()
    msg = 'Customer ID, First Name, Last Name, Address1, Address2, '
    msg = msg + 'City, State, Zip, email1, email2, phone1, phone2,'
    msg = msg + 'Group ID, Group, Current Points, Lifetime Points<br>'
    for c in customers:
        msg = msg + str( c.id) + ', ' + c.firstname + ', ' + c.lastname + ', '
        msg = msg + c.address1 + ', '+ c.address2 + ', ' + c.city + ', '
        msg = msg + c.state + ', ' + c.zip + ', ' + c.email1 + ', '
        msg = msg + c.email2 + ', ' + c.phone1 + ', ' + c.phone2 + ', '
        msg = msg + str( c.group.id) + ', '
        msg = msg + c.group.name_string() + ', ' + str( c.current_points) + ', '
        msg = msg + str( c.life_points) + '<br>'
    return HttpResponse( msg)





def orders_home(request):
    subgroup = 'Orders'
    all_links = []
    all_links.extend( [  Link( 'add', 'Add a Order' ) ] )
    all_links.extend( [ Link( 'list', 'List of Orders') ] )
    all_links.extend( [ Link( 'csv', 'List of Orders (csv format)') ] )
    context = {}
    context[ 'subgroup' ] = subgroup
    context[ 'all_links' ]= all_links
    return render( request, 'healthierhabits/common/home.html', context)


def orders_add( request):
    all_customers = Customers.objects.all()[::-1]
    all_rewards = Rewards.objects.all()[::-1]
    context = { 'all_customers' : all_customers, 'all_rewards' : all_rewards }
    return render( request, 'healthierhabits/orders/add.html', context)


def orders_add_action( request):
    order = Orders()
    order.customer = Customers.objects.get( id = request.POST[ 'customer'] )
    order.item = Rewards.objects.get( id = request.POST[ 'item'])
    order.price = request.POST[ 'price']
    order.date = timezone.now()
    order.filled = False
    order.save()
    context = { 'new_order' : [ order] }
    return render( request, 'healthierhabits/orders/add_confirm.html', context)


def orders_list(request):
    subgroup = 'Orders'
#    all_rows = Orders.objects.all()[::-1]
    all_rows = Orders.objects.order_by( '-date', 'customer__lastname', 'customer__firstname')
    context = {}
    context[ 'subgroup' ] = subgroup
    context[ 'all_rows' ] = all_rows
    return render( request, 'healthierhabits/common/list.html', context)


def orders_detail( request, orderid):
    order = Orders.objects.get( id=orderid)
    context = {}
    context[ 'order'] = order
    return render( request, 'healthierhabits/orders/detail.html', context)


def orders_csv( request):
    orders = Orders.objects.all()
    msg = 'Order ID, Customer ID, Customer, Date, Item, Price, '
    msg = msg + 'Filled<br>'
    for o in orders:
        msg = msg + str( o.id) + ', ' + str( o.customer.id) + ', '
        msg = msg + o.customer.name_string() + ', '
        msg = msg + o.date_string() + ', ' + o.item + ', '
        msg = msg + str( o.price) + ', ' + o.filled_yn() + '<br>'
    return HttpResponse( msg)


