# Chopin
Remember to be calm.
"Best Project with a Female Team Member, Best Potential Bad Girl Ventures Participant" winner Kent Fashion/Tech Hakathon 2016 
[devpost submission] (http://devpost.com/software/chopin)


## Inspiration
I recently purchased the Bellabeat Leaf wearable, which tracks activity, breathing and steps, but is unable to track heart rate. After using the Leaf for a month, I've found that the deep breathing exercises are often the most relaxing part of my day. I've even begun the habit of deep breathing whenever I feel anxious, which often mutes any stirring anxiety. 

However, sometimes I don't notice I'm beginning a stress episode until it's too late.  Speaking to another KFTH attendee today, I realized that I'm not the only one who this happens to. In this day and age, we're all frequently overwhelmed by the kind of stress that scatters your thoughts, glitches your words and turns simple tasks into complex challenges.

What's bothering anyone at the time of a stressful episode may be readily apparent emotionally, but it can be hard to pinpoint exactly at what point in the day you began going downhill, and what caused it. In addition, we often have biased perspectives of both our own actions and the actions of those around us that prevent us from seeing causation subjectively.

Chopin is smart, subjective solution to living a calmer, slower life. Chopin will be able to track your stress levels and analyze what exactly is bothering you. Chopin will sense when you're beginning to get anxious, and gently remind you to slow down and take a breath. 

You'll be able to make more informed decisions, and finally be able to breathe again. 

## What it does
Chopin's "pin" is **bandaged to the wrist by a strip of chiffon**. Alternatively, the pin can be strapped to the Bellabeat Leaf so that the sensor rests against the skin, **augmenting the wearable's functionality**.

The pin tracks your heartbeat, taking note of irregularities (speedups, slowdowns) and sending the data to the cloud to be analyzed. When your pulse quickens, Chopin will gently blink to indicate that you should slow down and do some deep breathing exercises.

Chopin will provide reports on your most relaxed and most stressful moments. You'll be able to notice weekly, monthly and even seasonal patterns.  Integrating with google calendars, Chopin can even figure out what you were doing at the time. 

## How I built it

Chopin's hardware consists of a heartrate moniter and LED attatched to a raspberry pi running Python.

The script then can regularly transmit data to the **AWS cloud** via MQTT messaging to be analyzed, and the user can use a web interface to review data.

## Challenges I ran into

Configuring Chopin to communicate with my Amazon AWS instance was problematic and I was unable to finish it before the deadline.  In addition, the heartbeat moniter is sometimes overly sensitive and records movements as heartbeats.

## What's next for Chopin
Once done debugging hardware, I would like to continue prototyping both the wearable and the app.

For the wearable, I would like to keep it in a small encasing that easily attatches to fabrics and jewelry. It will use Bluetooth Low Energy to eventually communicate with a phone app to cut out the bulk of the pi. I would also prefer to replace the glowing light stress alarm with a soft vibration.

In addition, Chopin's reporting capabilities willl expand beyond google maps. Chopin will one day look at social media posts, pictures, the news, and weather to suggest what may be bothering you and how to solve it. Chopin will also offer meditation and breathing exercises, during which your hearbeat and breathing will be tracked by the wearable to help establish progress and improvement.

**I hope to see Chopin become a commercial product in the near future**, so people like me and Dina can have **help navigating the chaos of modern day life.**
