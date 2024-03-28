import graphene
from graphene_django import DjangoObjectType
from .models import Room


class ChatType(DjangoObjectType):
    class Meta:
        model = Room
        fields = ['id', 'name', 'slug', 'color', 'creation_date']


class Query(graphene.ObjectType):
    read_chat = graphene.Field(ChatType, id=graphene.ID())
    chats = graphene.List(ChatType)

    def resolve_chats(self, info, **kwargs):
        return Room.objects.all()

    def resolve_read_chat(root, info, id):
        return Room.objects.get(id=id)


class CreateChat(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        slug = graphene.String()
        color = graphene.String()

    ok = graphene.Boolean()
    chat = graphene.Field(ChatType)

    def mutate(self, info, name, slug, color):
        chat = Room(name=name, slug=slug, color=color)
        chat.save()
        return CreateChat(ok=True, chat=chat)


class DeleteChat(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(self, info, id):
        restaurant = Room.objects.get(id=id)
        restaurant.delete()
        return DeleteChat(ok=True)


class UpdateChat(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        color = graphene.String()
        slug = graphene.String()

    ok = graphene.Boolean()
    chat = graphene.Field(ChatType)

    def mutate(self, info, id, name, slug, color):
        chat = Room.objects.get(id=id)
        chat.name = name
        chat.color = color
        chat.slug = slug
        chat.save()
        return UpdateChat(ok=True, chat=chat)


class Mutation(graphene.ObjectType):
    create_chat = CreateChat.Field()
    delete_chat = DeleteChat.Field()
    update_chat = UpdateChat.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



