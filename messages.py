message1 = "Communication is going to be a bit strained today -- don't take things personally." #aries
message2 = 'People may show their affection for you in odd ways -- be prepared to be confused.' #taurus
message3 = "You've been out of the social loop, but it's time to insert yourself back into it!" #gemini
message4 = "It's apparent that your charm is strong enough to overcome anyone's selfishness." #cancer
message5 = 'Think about long term gains in your finances today, and be try to be more thrifty.' #leo
message6 = 'Write out your feelings today -- the physical act will help you understand them.' #virgo
message7 = "Empty a few closets today -- the 'emotional' and 'linen' kinds. Get a fresh start." #libra
message8 = 'Share a new experience with someone who you want to get to know better today.' #scorpio
message9 = "Don't rush around making plans -- too many details that still need to be covered!" #sagittarius
message10 = 'The time is right to get active -- if you are having any doubts, just ignore them.' #capricorn
message11 = "Today you'll be placed in a leadership role that will be flattering, but not easy." #aquarius
message12 = 'The worst thing you can do today is let yourself get intimidated by expectations!' #pisces

first = ["Communication is going to be a bit strained today -- don't take things personally.", 'People may show their affection for you in odd ways -- be prepared to be confused.',
         "You've been out of the social loop, but it's time to insert yourself back into it!", "It's apparent that your charm is strong enough to overcome anyone's selfishness.",
         'Think about long term gains in your finances today, and be try to be more thrifty.']
second = ['Write out your feelings today -- the physical act will help you understand them', "Empty a few closets today -- the 'emotional' and 'linen' kinds. Get a fresh start",
          'Share a new experience with someone who you want to get to know better today', "Don't rush around making plans -- too many details that still need to be covered",
          'The time is right to get active -- if you are having any doubts, just ignore them']
third = ["Today you'll be placed in a leadership role that will be flattering, but not easy.", 'The worst thing you can do today is let yourself get intimidated by expectations!',
         'Becoming a member is the first step to becoming a leader, so find a group today.', "Your career isn't perfect, but there is a light at the end of the tunnel today.",
         "This is a great day for action, but it's not such a great day for deep thinking."]
fourth = ["It won't be an easy day for you, but it could be a very pivotal one. Hang in there.", "Exploration is the best thing for getting your juices going -- discovery is good.",
          "You've got more freedom than ever before but are you truly making the most of it?", "Your romance skills may not be the best, but that shouldn't stop you from flirting.",
          "If other people around you get loud and angry today, do not follow their example!"]
fifth = ["Every good thing must come to an end, but now you'll have time for something new", "Enjoy the page you are turning in life -- you are on to bigger and better things",
         'Introspection gives you strength, especially if you think about what makes you mad', "Fight the seduction of passivity today and initiate at least one new plan instead",
         "Other people's money will cause you more stress today than your own money will"]

sentences = [first, second, third, fourth, fifth]

for sentence in sentences:
    for element in sentence:
        element = element.strip()
