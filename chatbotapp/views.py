from django.shortcuts import redirect, render
from chatbot.settings import GENERATIVE_AI_KEY
from chatbotapp.models import ChatMessage
import google.generativeai as genai
import markdown

def send_message(request):
    if request.method == 'POST':
        # Configuring the AI API
        genai.configure(api_key=GENERATIVE_AI_KEY)
        model = genai.GenerativeModel("gemini-pro")

        # Retrieving the user's message
        user_message = request.POST.get('user_message')
        
        # Generating a bot response using the AI model
        bot_response = model.generate_content(user_message)

        # Convert the bot response from Markdown to HTML
        bot_response_html = markdown.markdown(bot_response.text)

        # Storing the user message and bot response (as HTML) in the database
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response_html)

    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot/list_messages.html', { 'messages': messages })

def clear_chat(request):
    if request.method == 'POST':
        ChatMessage.objects.all().delete()  # Delete all chat messages
    return redirect('list_messages')