from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import DetailSignsSerialiser, SignsRoadSerializer, CategorySignsSerializer
from .models import SignsRoad, CategorySigns
from rest_framework.decorators import api_view


@api_view(['GET'])
def category_signs_list( request):
    category = CategorySigns.objects.all()
    serialiser = CategorySignsSerializer(category, many=True)
    serialiser_data = {
        "category": serialiser.data,
        "status": "success",
        "status_code": status.HTTP_200_OK
    }
    return Response(serialiser_data)


@api_view(['GET'])
def signs_road_list(request):
    signs = SignsRoad.objects.all()
    serializer = SignsRoadSerializer(signs, many=True)
    serializer_data = {
        "signs": serializer.data,
        "status": "success",
        "status_code": status.HTTP_200_OK
    }
    return Response(serializer_data)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        signs = SignsRoad.objects.get(pk=pk)
        signs.delete()
        serializer_data = {
            "signs": "deleted",
            "status": "success",
            "status_code": status.HTTP_200_OK
        }
    except Exception as e:
        serializer_data = {
            "signs": str(e),
            "status": "success",
            "status_code": status.HTTP_404_NOT_FOUND
        }
    finally:
        return Response(serializer_data)


@api_view(['POST'])
def create(request):
    serializer = SignsRoadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_put(request, pk):
    try:
        signs = SignsRoad.objects.get(pk=pk)
        serialier = SignsRoadSerializer(signs, data=request.data)
        if serialier.is_valid():
            serialier.save()
            serialier_data = {
                "signs": serialier.data,
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
    except Exception as e:
        serialier_data = {
            "error": str(e),
            "ststus": "error",
            "status_code": status.HTTP_404_NOT_FOUND
        }
    finally:
        return Response(serialier_data)


@api_view(['PATCH'])
def update_patch(request, pk):
    try:
        signs = SignsRoad.objects.get(pk=pk)
        serialier = SignsRoadSerializer(signs, data=request.data)
        if serialier.is_valid():
            serialier.save()
            serialier_data = {
                "signs": serialier.data,
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
    except Exception as e:
        serialier_data = {
            "error": str(e),
            "ststus": "error",
            "status_code": status.HTTP_404_NOT_FOUND
        }
    finally:
        return Response(serialier_data)