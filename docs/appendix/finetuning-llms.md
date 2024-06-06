<style type="text/css">

.focus {
  color: var(--theme-foreground-focus);
}

.invert {
  background-color: var(--theme-foreground-alt);
  color: var(--theme-background);
}

.crop {
  border-radius: 8px;
  margin: 1rem;
  max-width: calc(50% - 2rem);
  box-shadow: 0 0 0 0.75px rgba(128, 128, 128, 0.2), 0 6px 12px 6px rgba(0, 0, 0, 0.4);
  aspect-ratio: 3024 / 1888;
  object-fit: cover;
  object-position: 0 100%;
}

.wbr::before {
  content: "\200b";
}

.wide {
  max-width: 960px;
}

figcaption code {
  font-size: 90%; /* TODO move to global.css */
}

</style>


# Fine-tuning LLMs

I like to believe that fine-tuning llms will solve many of my problems when it come to identifying computational works. I don't know to what extent this point of view is shared, but i feel that fine-tuning is one of the things where at first it feels like it should be easy (aka many tutorials out there, and libraries that provide oneliners to make it work), but is actually very time consuming. Here are the main point of contentions i struggled to understand:

#### The original choice: choosing your finetuning library

Working with LLMs means to resolve signal from all the hype that is out there. For instance, as I was looking around, the [Unsloth](https://github.com/unslothai/unsloth) library seemed to become very fashionable, making big claims about efficiency. Honestly I just don't know, all the youtube video and subreddits look like it was bot driven. Maybe it is legit, but I remain unconvinced at first glance.

The default libraries are usually a good starting point. I think most people will use the huggingface pipeline, in particular the `SFTtrainer` (part of the [trl](https://github.com/huggingface/trl) library) method for fine-tuning (as of 2024-06-05). But when `Meta` released their stuff, all their examples were in [torchtune](https://github.com/pytorch/torchtune). Besides `torchtune` and `SFTrainer`, there is [litgpt](https://github.com/Lightning-AI/litgpt/tree/main) and [axolotl](https://github.com/OpenAccess-AI-Collective/axolotl). They all kinda offering the same things, but they are all from different communities. Which one should you use?

One strategy is just to stick with the default `SFTtrainer` and be done with it. No question ask. In doing so, you might loose the perks of other libraries, but who care if `SFTtrainer` works right. 

Yet another strategy is to glance at the documentation for your task at hand, and pick the one that make most sense for you. I personally find that, sometimes, the huggingface documentation is confusing. `litgpt` is a bit better in this regard, as it is developped by [Sebastian Raschka](https://github.com/rasbt), a well known communicator in the realm transformers. 

A third strategy is to look at project health and the community underlying the library. The `axolotl` library would be a good bet, as it is developed by the [OpenAccess-AI-Collective](https://github.com/OpenAccess-AI-Collective). Contrary to the other libraries, `axolotl` is not backed by either a start-up like lightningAI or huggingface or a GAFA (which might be a good or a bad thing depending on your worldview). They have a large community of contributors and it is actively developped. A good way to assess the size and diversity of the community and project health is by looking at `Insights > Contributors` on the repository, as well as the ratio of open-issues / closed-issues. Then you can see if this is a community effort or a one-guy effort. Similarly, if you care about trying more models than just, say, llama, then it is relevant to know that `torchtune` is developped by Meta. I feel they will put less effort in supporting other libraries, especially when they come from the other GAFA who release weights of their models (microsoft's Phi3 or Google's Gemma family). This strategy to choose a library is definitely more involved, as it requires to understand the different actors in genAI, and balanced them with your own goals. 

### Where the data is coming from matters

It is good to keep in mind that which data has been used for pretraining can have a big impact on finetuning, as finetuning is simply a continuation of pretraining (see [FineWeb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) for a great overview of how it can be the case). But as users we don't have much control over that. 

### Tokenizers

Similar to data, tokenizing matters for the success or failure of finetuning. But we don't have much control over that. We just need to understand it a little bit.

### Model data format

When you are not used to it, i think that first working with neural network weights can be a bit confusing. With Llama3, sometimes you get a single file with the extension `.pth` (or `.pt`, i assume they are the same), and some other times there are multiple files with `safetensors` in the file name. The first one is a file that is proper to pytorch, while the second one is the huggingface format. One day, you hit the right reference that explains it to you (for me, it was [this one](https://pytorch.org/torchtune/main/deep_dives/checkpointer.html#understand-checkpointer)). And this is not magical at all. But still, I thought it was more confusing than at first.

### Base model vs instruct: which one should you use?

The `base` model is often useless, except if you have a lot of data. The `instruct` version is thought to be more useful, in that when you chat with it it doesn't return garbage, or doesn't start repeating the same word over and over again. That said, for some communities, `instruct` is annoying because it has been aligned with a certain set of values. 

### Prompt engineering

Knowing about prompt format/special tokens,  grammars, padding, function calls, etc... This is where it gets a bit overwhelming.

#### Prompt formats

When finetuning, there are different prompt formats that are related to how the model was trained (see [here](https://pytorch.org/torchtune/0.1/api_ref_data.html) for the main ones). It is not always clear which one is best. 

### Lora, QLora, adapters, quantization, RED, Reft, etc, etc...

It is easy to get lost in all the bells and whistles that make LLMs usable on modest hardware. In one sense, this is great because it means there is alot of research for the massed who are 'gpu-poor' to benefit from LLMs. But it can be a bit overwhelming. I often find myself forgetting details because I keep being hit by deluge of tutorials wanting to explain everything at once.

A key family of models are parameter-efficient fine tuning methods such as Lora, or Low-rank adaptation of LLMs, and quantized Lora (not the same as quantization). 

### Project management

How do you stay organized with all of that. There is a garden of forking path.
