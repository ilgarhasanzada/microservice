from rest_framework.serializers import ModelSerializer
from product.models import Product
from rest_framework import serializers

class ProductSerializer(ModelSerializer):
    current_user = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_current_user(self, obj):
        # Serializer içinde, request objesine erişim sağlamak için
        request = self.context.get('request')
        
        if request and request.user.is_authenticated:
            # Auth olmuş kullanıcı bilgisini döndür
            return {
                'user_id': request.user.id,
                'username': request.user.username,
                'email': request.user.email,
                # Diğer kullanıcı özellikleri ekleyebilirsiniz
            }
        
        # Eğer auth olmuş bir kullanıcı yoksa, boş bir sözlük döndür
        return {}