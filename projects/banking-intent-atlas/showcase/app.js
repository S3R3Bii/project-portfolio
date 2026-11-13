import {summarize,curve} from './metrics.mjs';
const $=id=>document.getElementById(id), pct=n=>(n*100).toFixed(1)+'%', label=s=>s.replaceAll('_',' ');
let evidence;
function node(tag,attrs={},text){const n=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);if(text!==undefined)n.textContent=text;return n;}
function draw(model,result){
  const svg=$('curve');for(const n of [...svg.children])if(!['title','desc'].includes(n.tagName))n.remove();
  const x=v=>64+v*580,y=v=>287-v/0.15*235;
  for(let t=0;t<=100;t+=20){svg.append(node('line',{x1:x(t/100),x2:x(t/100),y1:52,y2:287,stroke:'#e6ecee'}),node('text',{x:x(t/100),y:310,'text-anchor':'middle'},t+'%'));}
  for(let t=0;t<=15;t+=5){svg.append(node('line',{x1:64,x2:644,y1:y(t/100),y2:y(t/100),stroke:t===5?'#9aabb3':'#e6ecee','stroke-dasharray':t===5?'4 4':'none'}),node('text',{x:54,y:y(t/100)+4,'text-anchor':'end'},t+'%'));}
  svg.append(node('text',{x:354,y:341,'text-anchor':'middle'},'Accepted queries / coverage'),node('text',{x:17,y:172,transform:'rotate(-90 17 172)','text-anchor':'middle'},'Error among accepted'));
  for(const [name,color,title] of [['lexical','#b45137','TF-IDF'],['semantic','#28748c','MiniLM']]){
    const data=curve(evidence.rows,name);svg.append(node('path',{d:data.map((r,i)=>(i?'L':'M')+x(r.coverage)+','+y(r.rate)).join(' '),fill:'none',stroke:color,'stroke-width':name===model?3:1.7,opacity:name===model?1:.65}));
    const lx=name==='lexical'?80:230;svg.append(node('line',{x1:lx,x2:lx+23,y1:25,y2:25,stroke:color,'stroke-width':3}),node('text',{x:lx+30,y:29},title));
  }
  if(result.accepted)svg.append(node('circle',{cx:x(result.coverage),cy:y(result.rate),r:6,fill:'#132e42',stroke:'white','stroke-width':2}));
}
function update(){
  const model=$('model').value,t=Number($('cutoff').value),s=summarize(evidence.rows,model,t);
  $('cutoff-value').textContent=t.toFixed(2);
  $('policy-note').textContent=t===evidence.frozen[model]?'Frozen policy: this cutoff was selected before final test scoring.':'Exploration only: this cutoff is not the published frozen policy. Test outcomes must not be used to retune it.';
  $('accepted').textContent=s.accepted.toLocaleString()+' / '+pct(s.coverage);
  $('review').textContent=s.review.toLocaleString()+' queries';
  $('errors').textContent=s.accepted?s.errors.toLocaleString()+' / '+pct(s.rate):'No accepted queries';
  $('interval').textContent=s.interval?s.interval.map(pct).join('–'):'Not defined';draw(model,s);
}
function examples(){
  const container=$('examples');container.replaceChildren();
  for(const r of evidence.examples.filter(x=>x.kind===$('example-kind').value).slice(0,4)){
    const card=document.createElement('article');card.className='example';
    const q=document.createElement('blockquote');q.textContent='“'+r.text+'”';card.append(q);
    const dl=document.createElement('dl');
    for(const [term,value] of [['Benchmark label',label(r.truth)],['Model suggestion',label(r.prediction)+' · '+pct(r.confidence)]]){const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=term;dd.textContent=value;if(term==='Model suggestion'&&r.truth!==r.prediction)dd.className='wrong';dl.append(dt,dd);}card.append(dl);
    const alt=document.createElement('p');alt.className='alternatives';alt.textContent='Other candidates: '+label(r.runner_up)+' ('+pct(r.runner_up_probability)+'); '+label(r.third)+' ('+pct(r.third_probability)+').';card.append(alt);container.append(card);
  }
}
try{
  const response=await fetch('./evidence.json');if(!response.ok)throw new Error('Evidence request failed');evidence=await response.json();
  if(evidence.rows.length!==3080)throw new Error('Evidence row count differs from the reviewed release');
  $('cutoff').addEventListener('input',update);$('model').addEventListener('change',()=>{$('cutoff').value=evidence.frozen[$('model').value];update();});
  $('reset').addEventListener('click',()=>{$('cutoff').value=evidence.frozen[$('model').value];update();});$('example-kind').addEventListener('change',examples);update();examples();
}catch(error){$('policy-note').textContent='The saved evidence could not load. The reviewed paper and source repository remain available above.';for(const el of document.querySelectorAll('button,select,input'))el.disabled=true;console.error(error);}
