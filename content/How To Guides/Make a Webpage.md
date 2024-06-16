---
title: "Making a Data Dancers Webpage"
description: How to make a Hugo page with Data Dancers
---

# Publishing Content

There are two main points we need to consider: The **content** you want to publish (the **copy**) and the **metadata** about it (the **frontmatter**).

This guide wants to help you share your words with the world. Hope it helps!

- [Copy](#copy)
- [Frontmatter](#frontmatter)
  - [Required Fields](#required-fields)
- [Creating a File](#creating-file)
- [Run a Development Server](#run-a-development-server)
- [Write the Content](#writing-content)
- [Publish your Content](#publish-your-content)
- [Optional Fields](#optional-fields)
  - [Types and examples](#types-and-examples)
  - [Specifications](#specifications)

## Copy  {#copy}

A page  has **content** that adds value to your friends' lives. It can include 
  - A livecode tool or etude
  - A page about yourself
  - A meetup event
  - A how-to guide

## Frontmatter  {#frontmatter}

We need to help Hugo know how to publish this **content** for us. They call it **frontmatter**, and it looks like key/value pairs of metadata that goes at the top of a file. There is **one** field that is **required**, and the **rest** are **optional**.


### Required Fields {#required-fields}

> `title: string    example: "Making a Data Dancers Webpage"`

A page needs a `title`. This is a **string** that should be short or up to sentence length. The `title` enables your **content** to get its own URL we can visit. 

```
title: string        example: "Making a Data Dancers Webpage"
```

There are more fields available for increasing the resolution of your contribution [below](#optional-fields)

## Creating a File {#creating-file}

Does your **content** fit into one of these **categories**? 
- Algoraving
- How To Guides
- Livecoding
- Meetups

Then we've got a **category** for you!

Look in the `content` directory to find the directory that best matches your content. Then write a new file to start your draft. For example, a page named "Writing Code" has a filename "Writing Code.md" and is saved in `content/How To Guides/Writing Code.md`

If you don't see a directory that fits your **content**, you can add your page as a top level file.

Let's look at a file you already have called `content/da-da.md`. It doesn't show up in any category archives. And we can still see it when we link to it [directly](/da-da.md)!

## Run a Development Server {#run-a-development-server}

It is so easy to see your changes instantly. Hugo will watch your files for changes and instantly build and reload your browser. 

To start the development server:
```
hugo serve
```

Then you can open [localhost:1313](http://localhost:1313) and start hacking!

## Write the Content {#writing-content}

Once you've saved your file, let's put some text in it!

The top starts with the **frontmatter** and below goes your \***markdown**. 


*Hugo does some preprocessing of the markdown you write. It won't always feel like GitHub's markdown parser, so heads up if you find any surprises writing `my file.md`. 

## Publish your Content {#publish-your-content}

Once you are ready to share your stuff, push it up to GitHub! 

You should use whatever git software you already use now. If it is a desktop app, you might need to add the repository there. 

Here's a classic way to share your work using **bash**:


```
# Script to publish your changes. Replace <write me> with your values.

NEW_FILE=<write me>
COMMIT_MSG=<write me>
CURR_BRANCH=$(git branch --show-current)

# keep your work
git add $NEW_FILE
git commit -m $COMMIT_MSG


# pull in latest changes
git switch master
git pull 

# apply new additions to your local copy
git switch $CURR_BRANCH
git merge master

# share your branch to open a PR
git push

echo "Follow this link to open a PR for your changes on GitHub."
echo "https://github.com/data-dancers/data-dancers.github.io/compare/master...$CURR_BRANCH"
```

### Optional Fields  {#optional-fields}

Here are all of the optional parameters for describing your **content** with **frontmatter**. 

See below for individual descriptions. 


#### Types and examples   {#types-and-examples}

```
author: string       example: "Jane Doe"
date: date           example: 2024-06-16
link: string         example: "{{ .Site.baseURL }}/data-dancers"
image: string        example: "/images/data-dancers.jpg"
description: string  example: "A comprehensive guide to creating a Data Dancers webpage."
tags: array of strings     example: ["how-to", "guide", "data-dancers"]
categories: array of strings example: ["tutorial", "webpage"]
draft: boolean       example: false
slug: string         example: "making-a-data-dancers-webpage"
summary: string      example: "This guide walks you through the steps of creating a Data Dancers webpage."
keywords: array of strings  example: ["hugo", "frontmatter", "data-dancers"]
layout: string       example: "post"
featured: boolean    example: true
```

#### Specifications  {#specifications}

Here are some common optional fields you might use in the frontmatter, along with their types and examples:

    author: string example: "Jane Doe"

This field specifies the author of the **content**. It helps to attribute the work to a specific person.

    date: date example: 2024-06-16

The date the **content** was created or published. This helps in organizing and displaying **content** chronologically.

    link: string example: "https://example.com/data-dancers"

A URL relevant to the content, which could be an external link or related internal page.

    image: string example: "/images/data-dancers.jpg"

A path to an image associated with the content, often used for featured images or thumbnails.

    description: string example: "A comprehensive guide to creating a Data Dancers webpage."

A brief summary or description of the **content**. This is useful for SEO and providing readers with a quick overview.

    tags: array of strings example: ["how-to", "guide", "data-dancers"]

Tags associated with the **content** for easier categorization and search.

    categories: array of strings example: ["tutorial", "webpage"]

Categories under which the **content** falls, helping to organize the site **content**.

    draft: boolean example: false

A boolean value indicating if the **content** is a draft (true) or published (false).

    slug: string example: "making-a-data-dancers-webpage"

A URL-friendly version of the title, often used in the URL of the **content**.

    summary: string example: "This guide walks you through the steps of creating a Data Dancers webpage."

A short summary of the content, useful for previews or summaries on listing pages.

    keywords: array of strings example: ["hugo", "frontmatter", "data-dancers"]

Keywords relevant to the content, useful for SEO purposes.

    layout: string example: "post"

The layout template to be used for rendering the **content**. It helps Hugo apply the correct HTML structure.

    featured: boolean example: true

A boolean to mark if the **content** is featured (true) or not (false).