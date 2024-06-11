
<div class="grid grid-cols-2">
    <div>
        <h1>Scientific group life cycle</h1>
        <br>
        In this notebook, we explore the assumptions underlying the group-based computational hysteresis model. We start by providing an overview of the algebraic model, which is schematized in the figure on the right. We then explore the functions controlling the cost to learn programming, the group benefits of having programmers in your group, and recruitment process that are baked into the model.
        <br><br>
        <h2>Algebraic model</h2>
        <br>
        There are research groups ${tex`G`} with a number of non-programmers ${tex`n`} (blue nodes) and programmers ${tex`p`} (orange nodes). The schema represents the probability flow of moving across different states.<br><br> First, there is a constant rate of influx of students who do not know how to learn to code in research groups ${tex`\mu`}, represented by down arrows in the schema. We assume that groups have carrying capacity, K, limiting the inflow of new students.
        <br><br>
        Students can leave academia in one of two ways; graduation or trying to learn to code and fail (up arrows). We are interested in how the cost of learning to code ${tex`c(p,n)`} depends on the number of programmers and non-programmers within group. Diagonal arrows in the schema represent successful transition. We assume that programmers and non-programmers have different graduation rates, ${tex`\nu_p`} and ${tex`\nu_n`}, with ${tex`\nu_p > \nu_n`} (left and right arrows).<br><br>
        We model the group life cycle with the following master equation:
    </div>
    <div>
    <br><br><br><br><br><br><br><br><br>
        <img src="https://raw.githubusercontent.com/jstonge/modeling-comp-transition/main/figs/schema1.svg" alt="drawing" width="500"/>
    </div>
</div>

```tex
\begin{align*}
\frac{d}{dt}G_{n,p} &= \mu(G_{n-1,p} - G_{n,p}) + \nu_n \Big((n+1)G_{n+1,p}-nG_{n,p}\Big) \\
                           &+ \Big[ \tau_g(n+1,p-1)(1-c(n+1, p-1)G_{n+1,p-1} - \tau_g(n,p)G_{n,p} \Big] \\
                   &+ \nu_p\Big((p+1)G_{n,p+1} - pG_{n,p} \Big) \\
                   &+ \tau_g(n+1,p)(1-c(n+1,p))G_{n+1,p}
\end{align*}
```

Learning to code confers a collective benefits on individuals ${tex`\tau_g(n,p; \alpha, \beta) \propto \frac{\bar{Z}_{n,p}}{Z_{n,p}}`}, where

```tex
\begin{align*}
\log(Z_{n,p}) &\sim \alpha * n + \beta * p \\
\log(\bar{Z}_{n,p}) &\sim \alpha (n-1) +\beta (c * p + (1-c)(p+1))
\end{align*}
```

In a data-driven world, we assume that learning to code confer a large benefit to programmers over non-programmers such that ${tex`\alpha << \beta`}. We can think of ${tex`\bar{Z}_{n,p}`} as the potential benefits over ${tex`Z_{n,p}`}. Reorganizing the terms, we get:

```tex
\begin{align*}
\log\Big[\tau_g(n,p; \alpha, \beta))\Big] &= \alpha (n-1) +\beta (c * p + (1-c)(p+1)) - \alpha * n + \beta * p \\
                                  &= -\alpha + \beta(1-c)
\end{align*}
```

Note that ${tex`\tau_g`} ends up being a function of ${tex`n, p`} through the cost function:

```tex
c(n,p) = c_0*e^{-\frac{p}{n}}
```

We explore other potential cost functions below. We are interested in how programmers and non-programmers can coexists within this shifting environment, that we assume are confronting non-programmers to learn to code in various ways.

---

## Cost function (c)

#### Exponential

In the facetted plot below, we explore how different quantities impact our cost function. On the left, we have that the cost with respect to the ratio of programmers to non-programmers.  Number of non-programmers change as a function of group size _N_ and number of programmers _i_. On the right, we fix number of non-programmers at _10_, and we look at how adding programmers impact the cost. Implicitly, as we add more programmers the groups is getting bigger.

```js
const max_gr_size = 20
const l = view(Inputs.range([-1, -3], {value: -3, step: 1, label: "l"}))
```
```js
const N = view(Inputs.range([1, max_gr_size], {value: 20, step: 1, label: "group Size"}))
```
```js
const coder = view(Inputs.range([0, (N-1)], {value: 10, step: 1, label: "# coder"}))
```
```js
const c_0 = view(Inputs.range([0, 1], {value: 0.75, step: 0.01, label: "c₀"}))
```
```js
const nc = view(Inputs.range([1, N], {value: (N-coder), step: 1., label: "# non-coder", disabled:true}))
const nc_fixed = 10
```
```js
const non_coder = N - coder
const xs = [...Array(N).keys()];
```

```js
// i == p == # programmers
function cost_prog(n, i, c_0) { return c_0 * Math.exp(l*i/n); }
function cost_prog2(n, i, c_0) { return c_0 * Math.exp(l*i/(n+i)); }
```

<div class="grid grid-cols-2">
    <div class="card">${
        Plot.plot({
            title: `Groups fixed at N=${N} (#non-coders = ${N}-${coder} = ${N-coder} )`,
            height: 400, width: 600, grid: true,
            y: {
                label: "↑ c(non-prog,prog)", domain:[0,1.]
            },
            x: { label: "prog/non-prog →" },
            color: {
                domain: [
                    `${c_0} * Math.exp(${l}*${coder}/${non_coder})`,
                    `${c_0} * Math.exp(${l}*${coder}/(${non_coder}+${coder}))`,
                ],
                range: ["red", "green"],
                legend: true
            },
            marks: [
                Plot.lineY(xs.map(x => cost_prog(non_coder, x, c_0)), {stroke:"red"}),
                Plot.lineY(xs.map(x => cost_prog2(non_coder, x, c_0)), {stroke:"green"})
            ]
        })
    }
    <br><br>
    <em>What happens as you trade non coders for coders, while keeping the group size fixed>?</em>
    <p>Curent ratio: ${tex`p/n`} ${tex`\Rightarrow`} ${coder}/ ${non_coder} = ${(coder/(non_coder)).toFixed(2)}</p>
    <p style="color:red;">${tex`c(n,p)`} = ${cost_prog(coder, nc, c_0).toFixed(2)}</p>
    <p style="color:green;">${tex`c(n,p)`} = ${cost_prog2(coder, nc, c_0).toFixed(2)}</p>
    Non-programmers can still learn to code when ${tex`p=0`} because of ${tex`c_0`}<br><br>
    </div>
    <div class="card">${
        Plot.plot({
            title: "Number of non-coders fixed at 10",
            height: 400, width: 600, grid: true,
            y: {
                label: "↑ c(non-prog,prog)", domain:[0,1.]
            },
            x: { label: "prog →" },
            color: {
                domain: [
                    `${c_0} * exp(${l}*${nc_fixed}/#prog)`,
                    `${c_0} * exp(${l}*${nc_fixed}/(#prog+${nc_fixed}))`,
                ],
                range: ["red", "green"],
                legend: true
            },
            marks: [
                Plot.lineY(xs.map(x => cost_prog(nc_fixed, x, c_0)), {stroke:"red"}),
                Plot.lineY(xs.map(x => cost_prog2(nc_fixed, x, c_0)), {stroke:"green"}),
                Plot.ruleX(fooX, {
                    x: "x", y1:"y1", y2:"y2", stroke: ["orange", "lightblue"]
                }),
                Plot.arrow(fooY, {
                    y: "y", x1:"x1", x2:"x2", stroke: ["orange", "lightblue"]
                })
            ]
        })
    }
    <br><br>
    <em>What happens as you keep adding coders to non-coders groups?</em>
    </div>
</div>

```js
const fooX = [
    {"y2": cost_prog(nc_fixed,0,c_0), "y1":cost_prog(nc_fixed,1,c_0), "x": 0},
]

const fooY = [
    {"x2": 1, "x1":0, "y": cost_prog(nc_fixed,1,c_0)},
]
```

p.s. Recall that c=1 means that non-coders always fail to learn to code; c=0 means non-coders always succeed. Note that in the above function, we can play with $l$.

---

#### Inverse proportional

We can do something like ${tex`\frac{c_0}{1+k\frac{i}{n}}`} where ${tex`k \in R^+`} and is a constant . The gradual decrease as the number of programmers increases is less abrute than exponential.

```js
function cost_inverse(n, i, c_0, k) {
    return c_0 / (1 + k * (i / n));
}
```
```js
const k = view(Inputs.range([-3, 5], {value: 1, step: 0.1, label: "k"}))
```
```js
Plot.plot({
            height: 400, width: 600, grid: true,
            y: {
                label: "↑ c(non-prog,prog)", domain:[0,1.]
            },
            x: { label: "prog/non-prog →" },
            color: {
                domain: [
                    `${c_0} * Math.exp(${l}*${coder}/${non_coder})`,
                    `${c_0} / (1 + ${k} * (${coder} / ${non_coder}))`,
                ],
                range: ["black", "red"],
                legend: true
            },
            marks: [
                Plot.lineY(xs.map(x => cost_prog(non_coder, x, c_0))),
                Plot.lineY(xs.map(x => cost_inverse(non_coder, x, c_0, k)), {stroke:"red"})
            ]
        })

```

Movie showing the day to equilibrium with params:

```tex
\mu=0.1\ \nu_n=0.01\ \nu_p=0.03\ \alpha=0.01\ \beta=0.04\ \\
c_0=0.5\ K=40\ \text{max}1=40\ \text{max}2=40\ \text{Temp}=1
```

<div class="grid grid-cols-3">
    <div>
        <img src="../assets/movie2_ic0.gif" width=400>
    </div>
    <div>
        <img src="../assets/movie2_ic1.gif" width=400>
    </div>
    <div>
        <img src="../assets/movie2_ic3.gif" width=400>
    </div>
</div>
---

#### Elasticity

Based on **elasticity** from economics (basically there is some diminishin returns on investment), we can try ${tex`c_0\cdot(\frac{p}{n})^{-e}`}:

```js
function cost_elasticity(n, p, c_0) {
    let e = 0.5
    return c_0 * Math.pow((p / n), -e);
}
```

```js
Plot.lineY([...Array(20).keys()].map(x => cost_elasticity(10, x, 0.95))).plot({
    height: 400, width: 450, grid: true,
    y: { label: "↑ τ(α,β;n,p)" },
    x: { label: "p/n →" }
})
```

We could bound that so that this is between zero and one.

---

#### Sigmoid

In principle, we could go with a sigmoid. but I don't feel it make much sense to say that the first programmer is less useful than some midpoint. The following is the vanilla function

```tex
c_0 * \Big(1 - \frac{1}{1 + e^{-k * (i - m)}} \Big)
```

```js
function sigmoid_cost(n, i, c_0, k, m) {
    return c_0 * (1 - (1 / (1 + Math.exp(-k * (i - m)))));
}
```

```js
Plot.lineY([...Array(20).keys()].map(x => sigmoid_cost(10, x,  1.5, 0.5, 5))).plot({
    height: 400, width: 450, grid: true,
    y: { label: "↑ τ(α,β;n,p)" },
    x: { label: "p/n →" }
})
```

What if we modify it so that the cost remains constant at ${tex`c_0`} until it reaches a threshold of programmers to non-programmers, from which it decreases thereafter:

```tex
\text{sigmoid}(x) =
\begin{cases}
c_0 & \text{if } x < \frac{n}{p} \\
c_0 \cdot \frac{1}{1 + \exp\left(\alpha \left( \frac{n}{p} - x \right)\right)} & \text{if } x \geq \frac{n}{p}
\end{cases}
```

```js
function customSigmoid(n, p, c0, scale = 1) {
        const threshold = n / p;

        function sigmoid(x) {
            return 1 / (1 + Math.exp(scale * (threshold - x)));
        }

        function customFunction(x) {
            if (x < threshold) {
                return c0;
            } else {
                return c0 * sigmoid(x);
            }
        }

        return customFunction;
    }
```

```js
// Example usage:
``` 
```js
 const c0 = view(Inputs.range([0, 20], {value: 5, step: 1, label: "n"}));
 const n = view(Inputs.range([0, 20], {value: 10, step: 1, label: "n"}));
 
 const p = view(Inputs.range([0, 10], {value: 2, step: 1, label: "p"}));

 const scale = view(Inputs.range([-5, 5], {value: -3, step: 0.5, label: "scale"}));
```

```js
 const customFunc = customSigmoid(n, p, c0, scale)
```

```js
Plot.lineY(Array.from({length: 100}, (_, i) => i / 10).map(x => customFunc(x))).plot({
    height: 400, width: 450, grid: true,
    y: { label: "↑ τ(α,β;n,p)" },
    x: { label: "p/n →" }
})
```

---

## Group benefits (τ)

The group benefit looks like:

```tex
\tau_g(n,p,\alpha,\beta,b) = e^{-\alpha + \beta \cdot (1 - c(n,p,b=b))}
```

Group benefits is the extra humpf for the groups of having programmers. There is no world where adding programmers do not add benefits to your group (qualitative scientists might disagree here). The benefits of having programmers is weighted by the cost of learning to code. If the cost is zero, then everybody should just learn to code. If the cost is one (people always fail to become programmers when trying), the group benefits reduce to that of non-prorammers. With the exponential, we are assuming that the first programmer is twice as valuable as the second one. This might be a bit much. Here we start with ${tex`\beta`} being 10 times more than ${tex`\alpha`}.

```js
// i == p == # programmers
function tau(n, i, alpha, beta) {
    const c = cost_prog(n, i, 1)
    return Math.exp(-alpha + beta*(1 - c))
}

const tau_max_gr_size = 20
```
```js
const tau_alpha = view(Inputs.range([2, 4], {value: 1., step: 1, label: "α", format: x => 10**-x}))
const tau_beta = view(Inputs.range([1, 3], {value: 1., step: 1, label: "β", format: x => 10**-x}))
const tau_N = view(Inputs.range([0, tau_max_gr_size], {value: 20, step: 1, label: "group Size"}))
const tau_coder = view(Inputs.range([1, tau_max_gr_size], {value: 10, step: 1, label: "# coder"}))
```
```js
const tau_nc = view(Inputs.range([1, max_gr_size], {value: (tau_N-tau_coder), step: 1., label: "# non-coder", disabled:true}))
```

```js
const tau_non_coder = tau_N - tau_coder
```
```js
const tau_xs = [...Array(tau_N).keys()];
const tau_ys = tau_xs.map(x => tau(tau_non_coder, x, 10**-tau_alpha, 10**-tau_beta))
```
```js
Plot.lineY(tau_ys).plot({
    height: 400, width: 450, grid: true,
    y: { label: "↑ τ(α,β;n,p)" },
    x: { label: "p/n →" }
})
```

---

## Controlling the inflow and outflow of new students (σ)

<div class="grid grid-cols-3">
    <div class="grid-colspan-2">
        We now explore the ${tex`\sigma`} function, which is controlling non-programmers birth outflow and inflow.
        Right now we have<br><br>
        ${tex`\sigma(n, p, K, μ) = \mu\cdot(p+n+1)\cdot(1-\frac{1+p+n}{K})`}
        <br><br>
        In the code, we write:
        <ul>
            <li>${tex`G_{(n−1,p) \rightarrow (n, p)} = G_{n−1,𝑝} \cdot \sigma(n-1,p,K,\mu)`}  </li>
            <li>${tex`G_{(n+1,p) \rightarrow (n, p)}  = G_{n,p} \cdot \sigma(n,p,K,\mu)`}</li>
        </ul>
        Once again, we are modeling the probability flow from going in and out of any given state ${tex`G_{n,p}`}, say from moving to state with a single programmer (orange) and non-programmer (blue) to a state with a single non-programmer and two non-programmers. We assume that non-programmers coming in is part of a recruitment process, with groups exhibiting a carrying capacity.
    </div>
    <div>
        <br>
        <img src="https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/flow_birth.webp" alt="drawing" height=300>
    </div>
</div>

```js
function sigma(n,i,k,mu) {
    return mu*(i+n+1) * (1-(1+i+n)/k)
}
```

```js
const K = view(Inputs.range([10,30], {value: 25, step: 1, label: "K"}))
const mu = view(Inputs.range([0,1], {value: 0.01, step: 0.01, label: "μ"}))
```

```js
Plot.plot({
    height: 400, width: 450, grid: true,
    y: { label: "↑ σ(n,p,K,μ)" },
    x: { label: "p →" },
    marks: [
        Plot.lineY(xs.map(x => sigma(10, x, K, mu))),
    ],
    caption: "Number of non-programmers is fixed at 10. As you increase number of people getting closer to K, the recruitment process slow down. "
})
```

---


## Computational model

Code currently lives at [jstonge/modeling-comp-transition](https://github.com/jstonge/modeling-comp-transition)

```cpp
double cost(int n, int p, double c0) {
    double value = 0.0;
    if(n>0) value = c0/(1 + 1.0*(p/n));
    if(value<1 && value>0) return value;
    else return 0.0;
}

double tau(double a, double b, int n, int p, double c0) {
    double value = (-a+b*(1-cost(n,p,c0)));
    if(value>0) return value;
    else return 0.0;
}

double sigma(int n, int p, double k, double m) {
    double value = m*(n+p+1) * (1.0-(1.0+n+p)/(1.0*k));
    if(value>0) return value;
    else return 0.0;
}

int dydt(double t, const double y[], double f[], void * param) {
    [...]
    // Process all dynamics
    for(int d1=0; d1<p.max1; ++d1) {  //loop over number of non-programmers
    for(int d2=0; d2<p.max2; ++d2) { //loop over number of programmers

            fref[d1][d2] = 0;
            if(d1<p.max1-1) fref[d1][d2] -= sigma(d1,d2,p.K,p.mu)*yref[d1][d2]; //non-prog birth output
            if(d1>0) fref[d1][d2] += sigma(d1-1,d2,p.K,p.mu)*yref[d1-1][d2]; //non-prog birth input

            if(d1<p.max1-1) fref[d1][d2] += p.nu_n*(d1+1)*yref[d1+1][d2]; //non-prog death input
            fref[d1][d2] -= p.nu_n*d1*yref[d1][d2]; //non-prog death output

            if(d2<p.max2-1) fref[d1][d2] += p.nu_p*(d2+1)*yref[d1][d2+1]; //prog death input
            fref[d1][d2] -= p.nu_p*d2*yref[d1][d2]; //prog death output

            if(d2>0 && d1<p.max1-1) fref[d1][d2] += tau(p.alpha, p.beta, d1+1, d2-1,p.c0)*(d1+1)*(1.0-cost(d1+1,d2-1,p.c0))*yref[d1+1][d2-1]; //non-prog to prog input
            fref[d1][d2] -= tau(p.alpha, p.beta, d1, d2,p.c0)*d1*(1.0-cost(d1,d2,p.c0))*yref[d1][d2]; //non-prog to prog output

            if(d1<p.max1-1) fref[d1][d2] += tau(p.alpha, p.beta, d1+1, d2,p.c0)*(d1+1)*cost(d1+1,d2,p.c0)*yref[d1+1][d2]; //non-prog death input due to cost
            fref[d1][d2] -= tau(p.alpha, p.beta, d1, d2,p.c0)*d1*cost(d1,d2,p.c0)*yref[d1][d2]; //non-prog death output due to cost

    }
    }
}
```

```julia
τ(n, i, α, β; b=.9) = exp(-α + β*(1 - c(n, i, b=b))) # group benefits
cost(n, i; a=3, b=0.9) = n == i == 0 ? b : b * exp(-a*i / n)  # cost function
σ(n, i; K=25, μ=0.1)  = μ*(i+n+1) * (1-(i+n+1)/K)

function life_cycle_research_groups!(du, u, p, t)
    for i=0:(P-1), n=0:(N-1)

        du[i,n] = 0
        (n+1) < N && ( du[i,n] -= σ(n, i, K=K, μ=μ) )*G[i,n] # non-prog birth output
        n > 0 && ( du[i,n] += σ(n-1, i, K=K, μ=μ) )*G[i,n-1] # non-prog birth input

        (n+1) < N && ( du[i,n] += νₙ*(n+1)*G[i,n+1] ) # non-prog death input
        du[i,n] -= n*ν*G[i,n]ₙ # non-prog death output

        (i+1) < P && ( du[i,n] += νₚ*(i+1)*G[i+1,n] ) # prog death input
        du[i,n] -= i*νₚ*G[i,n] # prog death output

        (i > 0 && (n+1) < N) && ( du[i,n] += (n+1)*τ(n+1, i-1, α, β, b=b)*(1-cost(n+1,i-1, b=b))*G[i-1,n+1] ) # non-prog to prog input
        (i+1) < P && ( du[i,n] -= n*τ(n, i, α, β, b=b)*(1-cost(n, i, b=b))*G[i,n] ) # non-prog to prog output

        ((n+1) < N && (i+1) < P) && ( du[i,n] += (n+1)*τ(n+1, i, α, β, b=b)*cost(n+1,i,b=b)*G[i,n+1] ) # non-prog death input due to cost
        (i+1) < P && ( du[i,n] -= n*τ(n, i, α, β, b=b)*cost(n,i,b=b)*G[i,n] ) # non-prog death output due to cost
end
```