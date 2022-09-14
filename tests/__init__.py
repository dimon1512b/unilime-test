def get_subscription_status(view):
    @wraps(view)
    def inner(request, *args, **kwargs):
        chargebee.configure(CHARGEBEE_APIKEY, CHARGEBEE_SITENAME)
        try:
            if request.user.is_staff:
                return view(request, *args, **kwargs)
            if subscription_id := request.user.subscription_id:
                result = chargebee.Subscription.list({
                    "customer_id[is]": subscription_id,  # user_subscription_id
                    'status[is]': 'active'
                })
                if not result:
                    return HttpResponse(status=403)
                else:
                    return view(request, *args, **kwargs)
            else:
                return HttpResponse(status=403)
        except chargebee.api_error.OperationFailedError as error:
            return HttpResponse(status=406, content=error)
    return inner


def get_request(request):
    try:
        dict_list = {}
        for key, value in request.POST.items():
            dict_list.update({key: value})
        for key, value in request.GET.items():
            dict_list.update({unquote(key): unquote(value)})
        try:
            for key, value in json.loads(request.body).items():
                dict_list.update({key: value})
        except:
            try:
                for key, value in request.data.items():
                    dict_list.update({key: value})
            except:
                pass
        return dict_list
    except Exception as e:
        logger.exception(f'*** {e} ***')
