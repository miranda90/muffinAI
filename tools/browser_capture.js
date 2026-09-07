/* Paste in the browser console or evaluate with your browser automation.
   Read-only: resolves to a JSON-serializable snapshot; does not transmit it.
   Pass selectors to window.muffinSnapshot([...]) to compare matching regions. */
window.muffinSnapshot = async function (selectors = ['body']) {
  await document.fonts.ready;
  await Promise.all(Array.from(document.images, img => img.decode().catch(() => null)));
  const properties = ['display','position','box-sizing','width','height','min-width','max-width',
    'padding-top','padding-right','padding-bottom','padding-left','margin-top','margin-right','margin-bottom','margin-left',
    'gap','row-gap','column-gap','grid-template-columns','flex-direction','flex-wrap','justify-content','align-items',
    'font-family','font-size','font-weight','font-style','line-height','letter-spacing','color','background-color',
    'background-image','background-size','background-position','border-radius','box-shadow','object-fit','object-position',
    'overflow','visibility','opacity','transform'];
  const style = (el,pseudo) => { const cs=getComputedStyle(el,pseudo);return Object.fromEntries(properties.map(p=>[p,cs.getPropertyValue(p)])); };
  const path = el => {
    if (el.id) return '#'+CSS.escape(el.id);
    if (!el.parentElement) return el.tagName.toLowerCase();
    return path(el.parentElement)+' > '+el.tagName.toLowerCase()+':nth-child('+(Array.from(el.parentElement.children).indexOf(el)+1)+')';
  };
  const candidates = selectors.flatMap(s => Array.from(document.querySelectorAll(s)));
  const all = selectors.length===1 && selectors[0]==='body' ? [document.body,...document.body.querySelectorAll('*')] : candidates;
  const nodes=Array.from(new Set(all)).filter(el=>!['SCRIPT','STYLE','LINK','META'].includes(el.tagName)).map(el=>{
    const rect=el.getBoundingClientRect();
    return {key:path(el),tag:el.tagName.toLowerCase(),text:el.children.length ? '' : el.textContent.trim(),
      box:{x:rect.x+scrollX,y:rect.y+scrollY,width:rect.width,height:rect.height},style:style(el),
      pseudo:Object.fromEntries(['::before','::after'].map(p=>[p,{content:getComputedStyle(el,p).content,style:style(el,p)}])),
      media:{src:el.currentSrc||el.getAttribute('src')||'',alt:el.getAttribute('alt'),poster:el.getAttribute('poster')},
      hidden:rect.width===0||rect.height===0};
  });
  return {url:location.href,viewport:{width:innerWidth,height:innerHeight,dpr:devicePixelRatio},
    fonts_ready:document.fonts.status==='loaded',overflow:document.documentElement.scrollWidth>innerWidth,nodes};
};
