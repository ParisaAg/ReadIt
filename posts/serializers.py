from rest_framework import serializers
from .models import Post,Vote



class PostSerializers(serializers.ModelSerializer):
    authour=serializers.ReadOnlyField(source='authour.username')
    authour_id=serializers.ReadOnlyField(source='authour.id')
    vote=serializers.SerializerMethodField()


    class Meta:
        model=Post
        fields=['id','title','urls','authour','created_at','updated_at','authour_id','vote']


    def get_vote(self,post):
        return Vote.objects.filter(post=post).count()



class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields=['voter','post']