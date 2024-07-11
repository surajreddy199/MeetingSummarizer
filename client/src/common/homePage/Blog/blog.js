import React from 'react';
import {Article} from '../../../ui';

import { blog01, blog02, blog03, blog04, blog05 } from './imports';

import './blog.css';

const blogLinks = [
    {
      title: 'Natural Language Processing Technology',
      imgUrl: blog01,
      link: 'https://medium.com/greyatom/a-dive-into-natural-language-processing-103ae9b0a588',
      text: "This post will take you a beginner's guide to Natural Language Processing. A language is a way we humans, communicate with each other. Each day we produce data from emails, SMS, tweets, etc. we must have methods to understand these type of data, just like we do for other types of data. We will learn some of the basic but important techniques in Natural Language Processing. In simple terms, Natural language processing (NLP) is the ability of computers to understand human speech as it is spoken. NLP helps to analyze, understand, and derive meaning from human language in a smart and useful way. NLP algorithms are machine learning algorithms based. NLP learns by analyzing a set of examples (i.e. a large corpus, like a book, down to a collection of sentences), and making a statistical inference, instead of coding large sets of rules. We can organize the massive chunks of text data and solve a wide...",
    },
    
    {
      title: 'Speech to Text Conversion',
      imgUrl : blog04,
      link: 'https://towardsdatascience.com/easy-speech-to-link-with-python-3df0d973b426',
      text: 'Speech is the most common means of communication and the majority of the population in the world relies on speech to communicate with one another. Speech recognition system...',
    }
  ];
    

const Blog = () => (
  <div className="bg11Blog sectionPadding" id="blog">
    <div className="bg11BlogHeading">
      <h1 className="gradientText">A lot is happening about this, <br /> Our Refrences for Deep Learning.</h1>
    </div>
    <div className="bg11BlogContainer">
      <div className="bg11BlogContainerGroupA">
        <Article imgUrl={blog01} title={blogLinks[0].title} link={blogLinks[0].link} textContent={blogLinks[0].text} />
      </div>
      <div className="bg11BlogContainerGroupB">
        {blogLinks.map((item, index) => 
            <>
            {index ? 
                <Article imgUrl={item.imgUrl} title={item.title} link={item.link} key={item.title + index} textContent={item.text} />
                :null
            }
        </>
      )}     
      </div>
    </div>
  </div>
);

export default Blog;
