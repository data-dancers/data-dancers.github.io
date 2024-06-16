---
title: "Making a Data Dancers Webpage"
---

# Publishing Content

There are two main points we need to consider: The **content** you want to publish (the **copy**) and the **metadata** about it (the **frontmatter**).

## Copy

A page needs to be something worth reading. It has content that adds value to your friends lives. It can include 
  - A how-to guide
  - A livecode tool or etude
  - A meetup event
  - A page about yourself

## Frontmatter

We need to help Hugo know how to publish this content for us. There is **one** field that is **required**, and the **rest** are **optional**.


### Required

> `title: string    example: "Making a Data Dancers Webpage"`

A page needs a `title`. This is a **string** that should be short or up to sentence length. The `title` enables your **content** to get its own URL we can visit. 

```
title: string        example: "Making a Data Dancers Webpage"
```

### Optional

Here are all of the optional parameters for describing your content with **frontmatter**. 

See below for individual descriptions. 


#### Types and examples 

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

#### Specifications

Here are some common optional fields you might use in the frontmatter, along with their types and examples:

    author: string example: "Jane Doe"

This field specifies the author of the content. It helps to attribute the work to a specific person.

    date: date example: 2024-06-16

The date the content was created or published. This helps in organizing and displaying content chronologically.

    link: string example: "https://example.com/data-dancers"

A URL relevant to the content, which could be an external link or related internal page.

    image: string example: "/images/data-dancers.jpg"

A path to an image associated with the content, often used for featured images or thumbnails.

    description: string example: "A comprehensive guide to creating a Data Dancers webpage."

A brief summary or description of the content. This is useful for SEO and providing readers with a quick overview.

    tags: array of strings example: ["how-to", "guide", "data-dancers"]

Tags associated with the content for easier categorization and search.

    categories: array of strings example: ["tutorial", "webpage"]

Categories under which the content falls, helping to organize the site content.

    draft: boolean example: false

A boolean value indicating if the content is a draft (true) or published (false).

    slug: string example: "making-a-data-dancers-webpage"

A URL-friendly version of the title, often used in the URL of the content.

    summary: string example: "This guide walks you through the steps of creating a Data Dancers webpage."

A short summary of the content, useful for previews or summaries on listing pages.

    keywords: array of strings example: ["hugo", "frontmatter", "data-dancers"]

Keywords relevant to the content, useful for SEO purposes.

    layout: string example: "post"

The layout template to be used for rendering the content. It helps Hugo apply the correct HTML structure.

    featured: boolean example: true

A boolean to mark if the content is featured (true) or not (false).