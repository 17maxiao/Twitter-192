from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
from main.models import Tweet, Hashtag, UserLikes

# Create your views here.

def splash_view(request):
	return render(request, "splash.html", {})

def profile_view(request):
	return render(request, "profile.html", {})

def login_view(request):
	return render(request, "login.html", {})

def home_view(request):
    if not request.user.is_authenticated: 
        return redirect('login/')
    
    if request.method == "POST":
        tweet = Tweet(
            body=request.POST['body'],
            author=request.user
        )

        tweet.save()
    tweets = Tweet.objects.all()

    if request.method == "POST":
        Hashtag.objects.all().delete()
        allTags = []
        for tweet in tweets:
            tags = [i.split(" ", 1)[0] for i in tweet.body.split("#")[1:]]
            for tag in tags:
                allTags.append(tag)
        allTagsSet = set(allTags)
        for i in allTagsSet:
            print(i)
            hashtag = None
            if len(Hashtag.objects.filter(body=i)) == 0:
                hashtag = Hashtag.objects.create(body=i)
            else:
                hashtag = Hashtag.objects.get(body=i)
            hashtag.hashToTweet.add(tweet)
            print(len(Hashtag.objects.all()))
    
        # likes.save()
        # likes.users.add(request.user) 
    hashtags = Hashtag.objects.all()
   # hashtags = Hashtag.objects.all()
    #render(request, "home.html", {'hashtags': hashtags})
    return render(request, "home.html", {'tweets': tweets, 'hashtags': hashtags})

def hashtag_view(request):
    hashtag = Hashtag.objects.get(id=request.GET['id'])
    print(hashtag.body)
    tweets = hashtag.hashToTweet.all()
    for twt in tweets:
        print("teehee")
        print(twt)
    return render(request, "hashtag.html", {"tweets" : tweets})

def login_account(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/home')
    else: 
        return redirect('/login?error=True')

def signup(request):
    user = User.objects.create_user(
        username = request.POST['username'],
        password = request.POST['password'],
        email = request.POST['email']
    )
    login(request, user)
    return redirect('/home')

def logout_view(request):
    logout(request)
    return redirect('/')

def delete_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if request.user == tweet.author:
        tweet.delete()
    return redirect('/home')

def like_view(request):
    #pass
    tweet = Tweet.objects.get(id=request.GET['id'])
    # numberlikes = tweet.UserLikes
    # numberlikes = UserLikes.objects.get(tweet=tweet)
    if len(tweet.likes.filter(user=request.user)) == 0:
        newlike = UserLikes(user=request.user.username)
        newlike.save()
        tweet.likes.add(newlike)
        tweet.save()

    tweets = Tweet.objects.all()
    return redirect('/home')
    # return render(request, "home.html", {'tweets': tweets})