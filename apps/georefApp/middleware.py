#__BEGIN_LICENSE__
# Copyright (c) 2017, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All rights reserved.
#
# The GeoRef platform is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#__END_LICENSE__

from django.http import HttpResponseForbidden


class ClosedBetaMiddleware(object):
    def process_request(self, request):
        if request.path.startswith('/public') or request.path == '/':
            return None
        if getattr(request, 'user', None) is None or request.user.is_anonymous():
            return HttpResponseForbidden('401 Sorry, MapFasten is in closed beta and you do not appear to be on the list of authorized testers.')
        return None
