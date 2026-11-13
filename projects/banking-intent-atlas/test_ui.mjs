import assert from 'node:assert/strict';
import fs from 'node:fs';
import {summarize} from './showcase/metrics.mjs';
const data=JSON.parse(fs.readFileSync(new URL('./showcase/evidence.json',import.meta.url)));
const checks=[];
const check=(name,fn)=>{fn();checks.push(name);};
for(const model of ['lexical','semantic']){
  check(model+' frozen counts and rates',()=>{const a=summarize(data.rows,model,data.frozen[model]),b=data.metrics[model].referral;for(const k of ['accepted','errors'])assert.equal(a[k],b[k]);assert.ok(Math.abs(a.coverage-b.coverage)<1e-12);assert.ok(Math.abs(a.rate-b.error_rate)<1e-12);});
  check(model+' extreme thresholds',()=>{assert.equal(summarize(data.rows,model,0).accepted,3080);assert.equal(summarize(data.rows,model,1.01).accepted,0);assert.equal(summarize(data.rows,model,1.01).interval,null);});
  check(model+' monotone accepted count',()=>{let last=3080;for(let i=0;i<=100;i++){const n=summarize(data.rows,model,i/100).accepted;assert.ok(n<=last);last=n;}});
}
check('Wilson known synthetic case',()=>{const rows=Array.from({length:100},(_,i)=>[i,0,i<5?1:0,1,0,1]);const a=summarize(rows,'lexical',.5);assert.equal(a.errors,5);assert.ok(Math.abs(a.interval[0]-.02154367915436796)<1e-12);assert.ok(Math.abs(a.interval[1]-.11175046923191914)<1e-12);});
// Minimal DOM event harness: exercises application paths, not browser layout.
class Element{
  constructor(tag='div'){this.tagName=tag;this.children=[];this.attributes={};this.listeners={};this.value='';this.textContent='';}
  setAttribute(k,v){this.attributes[k]=String(v);}
  append(...nodes){for(const n of nodes){n.parent=this;this.children.push(n);}}
  replaceChildren(...nodes){this.children=[];this.append(...nodes);}
  remove(){this.parent.children=this.parent.children.filter(x=>x!==this);}
  addEventListener(name,fn){this.listeners[name]=fn;}
}
const ids=['model','cutoff','cutoff-value','reset','policy-note','curve','accepted','review','errors','interval','example-kind','examples'];
const elements=Object.fromEntries(ids.map(id=>[id,new Element()]));
elements.model.value='semantic';elements.cutoff.value='0.66';elements['example-kind'].value='accepted_error';
globalThis.document={getElementById:id=>elements[id],createElement:tag=>new Element(tag),createElementNS:(_,tag)=>new Element(tag),querySelectorAll:()=>[elements.model,elements.cutoff,elements.reset,elements['example-kind']]};
globalThis.fetch=async()=>({ok:true,json:async()=>data});
await import('./showcase/app.js');
check('initial view reflects frozen policy',()=>{assert.match(elements.accepted.textContent,/2,755/);assert.match(elements['policy-note'].textContent,/Frozen policy/);assert.equal(elements.examples.children.length,4);assert.ok(elements.curve.children.some(x=>x.tagName==='circle'));});
check('slider changes counts and marks exploration',()=>{elements.cutoff.value='0';elements.cutoff.listeners.input();assert.match(elements.accepted.textContent,/3,080/);assert.match(elements['policy-note'].textContent,/Exploration only/);});
check('reset restores original policy',()=>{elements.reset.listeners.click();assert.equal(Number(elements.cutoff.value),.66);assert.match(elements.errors.textContent,/96/);});
check('model selection restores matching cutoff',()=>{elements.model.value='lexical';elements.model.listeners.change();assert.equal(Number(elements.cutoff.value),.88);assert.match(elements.accepted.textContent,/2,151/);assert.match(elements.errors.textContent,/54/);});
check('example filter replaces cards',()=>{elements['example-kind'].value='referred';elements['example-kind'].listeners.change();assert.equal(elements.examples.children.length,4);assert.ok(elements.examples.children[0].children[0].textContent.includes(data.examples.find(x=>x.kind==='referred').text));});
globalThis.fetch=async()=>({ok:false});const old=console.error;console.error=()=>{};
await import('./showcase/app.js?failure-path');console.error=old;
check('failed fetch disables misleading controls',()=>{assert.equal(elements.model.disabled,true);assert.match(elements['policy-note'].textContent,/could not load/);});
console.log(JSON.stringify({pass:true,checks,limitation:'Node event harness; no browser rendering or accessibility conformance test.'},null,2));
