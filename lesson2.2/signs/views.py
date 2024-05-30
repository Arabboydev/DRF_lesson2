from django.shortcuts import render, get_object_or_404
from rest_framework import status
from .serializers import CategorySingSerializer, SingRoadSerializer, DetailSingsRoadSerializer
from .models import CategorySings, SingsRoad
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView


# class CreateListSignsView(ListCreateAPIView):
#     queryset = SingsRoad.objects.all()
#     serializer_class = SingRoadSerializer


class ListCategoryAPIView(APIView):
    def get(self, request):
        category = CategorySings.objects.all()
        serializer = CategorySingSerializer(category, many=True)
        serializer_data = {
            "category": serializer.data,
            "status": "success",
            "status_code": status.HTTP_200_OK,
        }
        return Response(serializer_data)


class ListRoadSingAPIView(APIView):
    def get(self, request):
        model = SingsRoad.objects.all()
        serializer = SingRoadSerializer(model, many=True)
        serializer_data = {
            "model": serializer.data,
            "status": "success",
            "status_code": status.HTTP_200_OK,
        }
        return Response(serializer_data)


class SignsRoadDetailDeleteUpdate(APIView):
    def get(self, request, pk):
        try:
            sings = SingsRoad.objects.get(pk=pk)
            serializer = DetailSingsRoadSerializer(sings)
            serializer_data = {
                "model": serializer.data,
                "status": "success",
                "status_code": status.HTTP_200_OK,
            }
        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def delete(self, request, pk):
        try:
            sings = SingsRoad.objects.get(pk=pk)
            sings.delete()
            serializer_data = {
                "sings": "deleted",
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": "success",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def post(self, request, pk):
        try:
            road_sign = SingsRoad.objects.get(pk=pk)
            serializer = SingRoadSerializer(road_sign, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SingsRoad.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            signs = SingsRoad.objects.get(pk=pk)
            serializer = SingRoadSerializer(signs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "signs": serializer.data,
                    "status": "success",
                    'status_code': status.HTTP_200_OK
                }
        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
        }
        finally:
            return Response(serializer_data)

    def patch(self, request, pk):
        try:
            signs = SingsRoad.objects.get(pk=pk)
            serializer = SingRoadSerializer(signs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "signs": serializer.data,
                    "status": "success",
                    'status_code': status.HTTP_200_OK
                }
        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
        }
        finally:
            return Response(serializer_data)
#



# class SingsRoadDetail(APIView):
#     def get(self, request, pk):
#         try:
#             sings = SingsRoad.objects.get(pk=pk)
#             serializer = DetailSingsRoadSerializer(sings)
#             serializer_data = {
#                 "model": serializer.data,
#                 "status": "success",
#                 "status_code": status.HTTP_200_OK,
#             }
#         except Exception as e:
#             serializer_data = {
#                 "error": str(e),
#                 "status": "error",
#                 "status_code": status.HTTP_404_NOT_FOUND
#             }
#         finally:
#             return Response(serializer_data)
#
#
# class SingsRoadDelete(APIView):
#     def get(self, request, pk):
#         try:
#             sings = SingsRoad.objects.get(pk=pk)
#             sings.delete()
#             serializer_data = {
#                 "sings": "deleted",
#                 "status": "success",
#                 "status_code": status.HTTP_200_OK
#             }
#         except Exception as e:
#             serializer_data = {
#                 "error": str(e),
#                 "status": "success",
#                 "status_code": status.HTTP_404_NOT_FOUND
#             }
#         finally:
#             return Response(serializer_data)
#
#
# class SingsRoadPut(APIView):
#     def put(self, request, pk):
#         try:
#             signs = SingsRoad.objects.get(pk=pk)
#             serializer = SingRoadSerializer(signs, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 serializer_data = {
#                     "signs": serializer.data,
#                     "status": "success",
#                     'status_code': status.HTTP_200_OK
#                 }
#         except Exception as e:
#             serializer_data = {
#                 "error": str(e),
#                 "status": "error",
#                 "status_code": status.HTTP_404_NOT_FOUND
#         }
#         finally:
#             return Response(serializer_data)
#
#
# class SingsRoadPatch(APIView):
#     def patch(self, request, pk):
#         try:
#             signs = SingsRoad.objects.get(pk=pk)
#             serializer = SingRoadSerializer(signs, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 serializer_data = {
#                     "signs": serializer.data,
#                     "status": "success",
#                     'status_code': status.HTTP_200_OK
#                 }
#         except Exception as e:
#             serializer_data = {
#                 "error": str(e),
#                 "status": "error",
#                 "status_code": status.HTTP_404_NOT_FOUND
#         }
#         finally:
#             return Response(serializer_data)

# class CreateSignsRoadAPIView(APIView):
#     def post(self, request):
#         serialier = SingRoadSerializer(data=request.data)
#         if serialier.is_valid():
#             serialier.save()
#             return Response(serialier.data, status=status.HTTP_201_CREATED)
#         return Response(serialier.errors, status=status.HTTP_400_BAD_REQUEST)