
 <img  width="100%" src="images/seuss_flavor.jpg" alt="Seuss" /> 

___

<p float="center">
  <img img align="top" src="images/thing1.jpg" width="20%" />
  <img src="images/seuss_op.jpg" width="50%" /> 
  <img src="images/thing2.jpg" width="22%" />
</p>

<br/>


This is an example of exact output. All formatting is done with python and is written into the code. *More in depth explanation further* [below.](#explanation)


<br/><br/><br/>

## &emsp; **A Peek Into How Markov Works**


<img align="right" width="300" src="images/simple_marc.jpg" alt="Markov Chain Simple Graph">
    

&emsp; A Markov chain or Markov process is a *theoretical model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event*. Informally, this may be thought of as, <strong>What happens next depends only on the state of affairs now.</strong> Markov chains have many applications as statistical models of real-world processes. They are the basis for general theoretical simulation methods and have found application in a wide variety of fields.<br/>


&emsp; By convention, all possible states and transitions have been included in the definition of the process, so **there is always a next state, and the process does not terminate**. The transitions are often thought of as moments in time, but they can equally well refer to any other discrete measurement. The transitions are the integers, and the random process is a mapping of these states. <br/>

&emsp; Since **the system changes randomly, it is generally impossible to predict with certainty the state of a Markov chain at a given point in the future.** However, the statistical properties of the system's future can be predicted. In many applications, it is these statistical properties that are important.

<br clear="right"/>


<br/><br/><br/>

<p align="center">
<a href="https://www.youtube.com/embed/i3AkTO9HLXo"><img src="images/mc.jpg" alt="Markov Chains Clearly Explained! Part - 1" width="691" height="389" border="10" /></a>
</p>




<img align="right" src="images/nest_ex.png" alt="Example of what the created dictionary looks like using Red Fish, Blue Fish" width=20%>

## Explanation
### *Brief break down of the nuances of my code.


&emsp; First we start with importing text to train our model. This is especially fun because **you can use any text input you want.** Since I choose more of a lyrical text, I decided I wanted to keep contractions and, for output readability, discard all single letter words. Also, I left in commas and periods to help preserve sentence structure. Took forever, but i finally got the regex correct.</br>
<h4 align="right"> For those curious kids watching at home, the regex is r'[.,]|[a-z]+[']?[a-z]+' </h4>

</b>




##### Delving deep and almost losing my self in python's deep nested dictionaries. Holy crap, that almost broke my brain. 

&emsp; WOW! Iterating over each word in a text and recording every time  word that follows it over the entirety text and how many 


<br clear="right"/>

</br>
<br/><br/><br/><br/>
<img src="images/outputt.png" alt="Markov Scatter Graph" title="Markov Scatter Graph">



[![GitHub Streak](http://github-readme-streak-stats.herokuapp.com?user=brichavez&theme=dark&background=000000)](https://git.io/streak-stats)
