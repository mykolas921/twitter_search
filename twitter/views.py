import requests

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from.exceptions import TwitterAuthError
from .utils import get_access_token, base_url


class TwitterSearchView(APIView):
  permission_classes = (AllowAny, )

  def get(self, request):
    try:
      access_token = get_access_token()
    except TwitterAuthError as e:
      return Response(e.detail_json, status=e.status_code)

    # count should be in range(1,50)
    count = int(request.query_params.get('count') or 15)
    count = max(1, count)
    count = min(100, count)

    q = request.query_params.get('q')

    if q and count:
      search_params = {
        'q': q,
        'result_type': 'recent',
        'count': count
      }

      search_headers = {
        'Authorization': f'Bearer {access_token}'
      }
      search_url = f'{base_url}1.1/search/tweets.json'
      search_resp = requests.get(
        search_url,
        headers=search_headers,
        params=search_params
      )

      return Response(search_resp.json(), status=search_resp.status_code)
    else:
      return Response(
        {'error': 'Invalid q or count'},
        status=status.HTTP_400_BAD_REQUEST
      )

