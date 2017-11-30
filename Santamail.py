#!/usr/bin/env python
#totally wrote this on my phone... Probably buggy

#msg1 only has santa
msg1 = """
  Dear %s,
  
  Ho Ho Ho! Thanks for participating in the Hacker Secret Santa this year!!! We've had over 170 participants this year from 17 different countries (up from 40/7 last year) :D
  
   
  Again to remind you of the rules/notes  
  
  1. Soft limit of $25
  
  2. Try to have your gifts delivered by Christmas.
  
  3. Feel free to do some OSINT on the person who's name you've been given. Don't dox them or their loved ones, but if you can find out they prefer Star Wars vs Star Trek then that's ok.
  
  4. It's up to you if you want to tell them or not who the gift has come from.
  
  5. Have fun and use your imagination!!!
  
   
  Also, not really rules, but probably good to know....
   
  1. I won't share any of your data (other than with google and the person that gets you for secret santa)
  
  2. Last year we did have a few mix ups with foreign delivery services (*cough* DHL *cough*). So if you're somewhere outside of the US/Canada there's no guarantees on how soon you'll get your gifts.
  
  3. Seriously, don't fuck it up. We've had a pretty good rate of people delivering on it and I'd like to have it again next year. If for some reason you can't fulfill a gift, let me know and I'm sure someone would take over your spot.  
  
   
  DON'T FORGET to tweet out a picture or note of your gift with the HackerSanta hashtag!! We all love seeing the unique and thoughtful hackery things people have sent in the past.
  
  """ 
  #msg2 has santee,handle,address
  msg2 = """
  Your Hacker Secret Santa recipient is --
  
  %s with a handle of %s and their address is %s

     
  This message was automagically generated from a computer. 
  
  Nothing could possibly go wrong...
  """
  print msg1 % "Matt"
  print msg2 % ("steve","@steve","<steves address>")
