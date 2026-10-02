(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,434626,e=>{"use strict";var t=e.i(271645);let i=t.forwardRef(function(e,i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:2,stroke:"currentColor","aria-hidden":"true",ref:i},e),t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"}))});e.s(["ExternalLinkIcon",0,i],434626)},655063,e=>{"use strict";var t=e.i(540626),i=e.i(271645);e.s(["useDebouncedValue",0,function(e,s,n){let[a,r,o]=function(e,s,n){let[a,r]=(0,i.useState)(e),o=(0,t.useDebouncer)(r,s,n);return[a,o.maybeExecute,o]}(e,s,n);return(0,i.useEffect)(()=>{r(e)},[e,r]),[a,o]}],655063)},540626,e=>{"use strict";let t;var i=e.i(271645);let s=(0,i.createContext)(null);function n(e,t){if(Object.is(e,t))return!0;if("object"!=typeof e||null===e||"object"!=typeof t||null===t)return!1;if(e instanceof Map&&t instanceof Map){if(e.size!==t.size)return!1;for(let[i,s]of e)if(!t.has(i)||!Object.is(s,t.get(i)))return!1;return!0}if(e instanceof Set&&t instanceof Set){if(e.size!==t.size)return!1;for(let i of e)if(!t.has(i))return!1;return!0}if(e instanceof Date&&t instanceof Date)return e.getTime()===t.getTime();let i=a(e);if(i.length!==a(t).length)return!1;for(let s=0;s<i.length;s++)if(!Object.prototype.hasOwnProperty.call(t,i[s])||!Object.is(e[i[s]],t[i[s]]))return!1;return!0}function a(e){return Object.keys(e).concat(Object.getOwnPropertySymbols(e))}var r=e.i(430224);function o(e,t){return e===t}function l(e,t=e=>e,s){let n=s?.compare??o,a=(0,i.useCallback)(t=>{let{unsubscribe:i}=e.subscribe(t);return i},[e]),d=(0,i.useCallback)(()=>e.get(),[e]);return(0,r.useSyncExternalStoreWithSelector)(a,d,d,t,n)}function d(e,...t){return"function"==typeof e?e(...t):e}var u=class{#e=!0;#t;#i;#s;#n;#a;#r;#o;#l=0;#d=5;#u=!1;#c=!1;#p=null;#m=()=>{this.debugLog("Connected to event bus"),this.#a=!0,this.#u=!1,this.debugLog("Emitting queued events",this.#n),this.#n.forEach(e=>this.emitEventToBus(e)),this.#n=[],this.stopConnectLoop(),this.#i().removeEventListener("tanstack-connect-success",this.#m)};#g=()=>{if(this.#l<this.#d){this.#l++,this.dispatchCustomEvent("tanstack-connect",{});return}this.#i().removeEventListener("tanstack-connect",this.#g),this.#c=!0,this.debugLog("Max retries reached, giving up on connection"),this.stopConnectLoop()};#h=()=>{this.#u||(this.#u=!0,this.#i().addEventListener("tanstack-connect-success",this.#m),this.#g())};constructor({pluginId:e,debug:t=!1,enabled:i=!0,reconnectEveryMs:s=300}){this.#t=e,this.#e=i,this.#i=this.getGlobalTarget,this.#s=t,this.debugLog(" Initializing event subscription for plugin",this.#t),this.#n=[],this.#a=!1,this.#c=!1,this.#r=null,this.#o=s}startConnectLoop(){null!==this.#r||this.#a||(this.debugLog(`Starting connect loop (every ${this.#o}ms)`),this.#r=setInterval(this.#g,this.#o))}stopConnectLoop(){this.#u=!1,null!==this.#r&&(clearInterval(this.#r),this.#r=null,this.#n=[],this.debugLog("Stopped connect loop"))}debugLog(...e){this.#s&&console.log(`🌴 [tanstack-devtools:${this.#t}-plugin]`,...e)}getGlobalTarget(){if("u">typeof globalThis&&globalThis.__TANSTACK_EVENT_TARGET__)return this.debugLog("Using global event target"),globalThis.__TANSTACK_EVENT_TARGET__;if("u">typeof window&&void 0!==window.addEventListener)return this.debugLog("Using window as event target"),window;let e="u">typeof EventTarget?new EventTarget:void 0;return void 0===e||void 0===e.addEventListener?(this.debugLog("No event mechanism available, running in non-web environment"),{addEventListener:()=>{},removeEventListener:()=>{},dispatchEvent:()=>!1}):(this.debugLog("Using new EventTarget as fallback"),e)}getPluginId(){return this.#t}dispatchCustomEventShim(e,t){try{let i=new Event(e,{detail:t});this.#i().dispatchEvent(i)}catch(e){this.debugLog("Failed to dispatch shim event")}}dispatchCustomEvent(e,t){try{this.#i().dispatchEvent(new CustomEvent(e,{detail:t}))}catch(i){this.dispatchCustomEventShim(e,t)}}emitEventToBus(e){this.debugLog("Emitting event to client bus",e),this.dispatchCustomEvent("tanstack-dispatch-event",e)}createEventPayload(e,t){return{type:`${this.#t}:${e}`,payload:t,pluginId:this.#t}}emit(e,t){if(!this.#e)return void this.debugLog("Event bus client is disabled, not emitting event",e,t);if(this.#p&&(this.debugLog("Emitting event to internal event target",e,t),this.#p.dispatchEvent(new CustomEvent(`${this.#t}:${e}`,{detail:this.createEventPayload(e,t)}))),this.#c)return void this.debugLog("Previously failed to connect, not emitting to bus");if(!this.#a){this.debugLog("Bus not available, will be pushed as soon as connected"),this.#n.push(this.createEventPayload(e,t)),"u">typeof CustomEvent&&!this.#u&&(this.#h(),this.startConnectLoop());return}return this.emitEventToBus(this.createEventPayload(e,t))}on(e,t,i){let s=i?.withEventTarget??!1,n=`${this.#t}:${e}`;if(s&&(this.#p||(this.#p=new EventTarget),this.#p.addEventListener(n,e=>{t(e.detail)})),!this.#e)return this.debugLog("Event bus client is disabled, not registering event",n),()=>{};let a=e=>{this.debugLog("Received event from bus",e.detail),t(e.detail)};return this.#i().addEventListener(n,a),this.debugLog("Registered event to bus",n),()=>{s&&this.#p?.removeEventListener(n,a),this.#i().removeEventListener(n,a)}}onAll(e){if(!this.#e)return this.debugLog("Event bus client is disabled, not registering event"),()=>{};let t=t=>{e(t.detail)};return this.#i().addEventListener("tanstack-devtools-global",t),()=>this.#i().removeEventListener("tanstack-devtools-global",t)}onAllPluginEvents(e){if(!this.#e)return this.debugLog("Event bus client is disabled, not registering event"),()=>{};let t=t=>{let i=t.detail;this.#t&&i.pluginId!==this.#t||e(i)};return this.#i().addEventListener("tanstack-devtools-global",t),()=>this.#i().removeEventListener("tanstack-devtools-global",t)}};let c=new Map;function p(e){if(void 0!==e)try{return JSON.parse(JSON.stringify(e))}catch{return null}}let m=new class extends u{constructor(e){super({pluginId:"pacer",debug:e?.debug,reconnectEveryMs:1e3})}};function g(e,t,i){let s="object"==typeof e,n=s?e:void 0;return{next:(s?e.next:e)?.bind(n),error:(s?e.error:t)?.bind(n),complete:(s?e.complete:i)?.bind(n)}}let h=[],f=0,{link:x,unlink:b,propagate:v,checkDirty:_,shallowPropagate:y}=function({update:e,notify:t,unwatched:i}){return{link:function(e,t,i){let s=t.depsTail;if(void 0!==s&&s.dep===e)return;let n=void 0!==s?s.nextDep:t.deps;if(void 0!==n&&n.dep===e){n.version=i,t.depsTail=n;return}let a=e.subsTail;if(void 0!==a&&a.version===i&&a.sub===t)return;let r=t.depsTail=e.subsTail={version:i,dep:e,sub:t,prevDep:s,nextDep:n,prevSub:a,nextSub:void 0};void 0!==n&&(n.prevDep=r),void 0!==s?s.nextDep=r:t.deps=r,void 0!==a?a.nextSub=r:e.subs=r},unlink:function(e,t=e.sub){let s=e.dep,n=e.prevDep,a=e.nextDep,r=e.nextSub,o=e.prevSub;return void 0!==a?a.prevDep=n:t.depsTail=n,void 0!==n?n.nextDep=a:t.deps=a,void 0!==r?r.prevSub=o:s.subsTail=o,void 0!==o?o.nextSub=r:void 0===(s.subs=r)&&i(s),a},propagate:function(e){let i,s=e.nextSub;e:for(;;){let n=e.sub,a=n.flags;if(60&a?12&a?4&a?!(48&a)&&function(e,t){let i=t.depsTail;for(;void 0!==i;){if(i===e)return!0;i=i.prevDep}return!1}(e,n)?(n.flags=40|a,a&=1):a=0:n.flags=-9&a|32:a=0:n.flags=32|a,2&a&&t(n),1&a){let t=n.subs;if(void 0!==t){let n=(e=t).nextSub;void 0!==n&&(i={value:s,prev:i},s=n);continue}}if(void 0!==(e=s)){s=e.nextSub;continue}for(;void 0!==i;)if(e=i.value,i=i.prev,void 0!==e){s=e.nextSub;continue e}break}},checkDirty:function(t,i){let n,a=0,r=!1;e:for(;;){let o=t.dep,l=o.flags;if(16&i.flags)r=!0;else if((17&l)==17){if(e(o)){let e=o.subs;void 0!==e.nextSub&&s(e),r=!0}}else if((33&l)==33){(void 0!==t.nextSub||void 0!==t.prevSub)&&(n={value:t,prev:n}),t=o.deps,i=o,++a;continue}if(!r){let e=t.nextDep;if(void 0!==e){t=e;continue}}for(;a--;){let a=i.subs,o=void 0!==a.nextSub;if(o?(t=n.value,n=n.prev):t=a,r){if(e(i)){o&&s(a),i=t.sub;continue}r=!1}else i.flags&=-33;i=t.sub;let l=t.nextDep;if(void 0!==l){t=l;continue e}}return r}},shallowPropagate:s};function s(e){do{let i=e.sub,s=i.flags;(48&s)==32&&(i.flags=16|s,(6&s)==2&&t(i))}while(void 0!==(e=e.nextSub))}}({update:e=>e._update(),notify(e){h[w++]=e,e.flags&=-3},unwatched(e){void 0!==e.depsTail&&(e.depsTail=void 0,e.flags=17,k(e))}}),j=0,w=0;function k(e){let t=e.depsTail,i=void 0!==t?t.nextDep:e.deps;for(;void 0!==i;)i=b(i,e)}var N=class{constructor(e,i){this.atom=function(e){let i="function"==typeof e,s={_snapshot:i?void 0:e,subs:void 0,subsTail:void 0,deps:void 0,depsTail:void 0,flags:+!i,get:()=>(void 0!==t&&x(s,t,f),s._snapshot),subscribe(e){var i;let n,a,r=g(e),o={current:!1},l=(i=()=>{s.get(),o.current?r.next?.(s._snapshot):o.current=!0},n=()=>{let e=t;t=a,++f,a.depsTail=void 0,a.flags=6;try{return i()}finally{t=e,a.flags&=-5,k(a)}},a={deps:void 0,depsTail:void 0,subs:void 0,subsTail:void 0,flags:6,notify(){let e=this.flags;16&e||32&e&&_(this.deps,this)?n():this.flags=2},stop(){this.flags=0,this.depsTail=void 0,k(this)}},n(),a);return{unsubscribe:()=>{l.stop()}}},_update(n){let a=t,r=(void 0)??Object.is;if(i)t=s,++f,s.depsTail=void 0;else if(void 0===n)return!1;i&&(s.flags=5);try{let t=s._snapshot,a="function"==typeof n?n(t):void 0===n&&i?e(t):n;if(void 0===t||!r(t,a))return s._snapshot=a,!0;return!1}finally{t=a,i&&(s.flags&=-5),k(s)}}};return i?(s.flags=17,s.get=function(){let e=s.flags;if(16&e||32&e&&_(s.deps,s)){if(s._update()){let e=s.subs;void 0!==e&&y(e)}}else 32&e&&(s.flags=-33&e);return void 0!==t&&x(s,t,f),s._snapshot}):s.set=function(e){if(s._update(e)){let e=s.subs;if(void 0!==e&&(v(e),y(e),1)){for(;j<w;){let e=h[j];h[j++]=void 0,e.notify()}j=0,w=0}}},s}(e),this.get=this.get.bind(this),this.setState=this.setState.bind(this),this.subscribe=this.subscribe.bind(this),i&&(this.actions=i(this))}setState(e){this.atom.set(e)}get state(){return this.atom.get()}get(){return this.state}subscribe(e){return this.atom.subscribe(g(e))}};function C(){return{canLeadingExecute:!0,executionCount:0,isPending:!1,lastArgs:void 0,status:"idle",maybeExecuteCount:0}}let E={enabled:!0,leading:!1,trailing:!0,wait:0};var S=class{#f;constructor(e,t){this.fn=e,this.store=new N(C()),this.setOptions=e=>{this.options={...this.options,...e},this.#x()||this.cancel()},this.#b=e=>{this.store.setState(t=>{let i={...t,...e},{isPending:s}=i;return{...i,status:this.#x()?s?"pending":"idle":"disabled"}}),((e,t)=>{let i=t.key;if(i){var s,n;c.set(i,t),m.emit(e,{key:(s={...t,key:i}).key,store:{state:p("function"==typeof(n=s.store).get?n.get():n.state)},options:p(s.options)})}})("Debouncer",this)},this.#x=()=>!!d(this.options.enabled,this),this.#v=()=>d(this.options.wait,this),this.maybeExecute=(...e)=>{if(!this.#x())return;this.#b({maybeExecuteCount:this.store.state.maybeExecuteCount+1});let t=!1;this.options.leading&&this.store.state.canLeadingExecute&&(this.#b({canLeadingExecute:!1}),t=!0,this.#_(...e)),this.options.trailing&&this.#b({isPending:!0,lastArgs:e}),this.#f&&clearTimeout(this.#f),this.#f=setTimeout(()=>{this.#b({canLeadingExecute:!0}),this.options.trailing&&!t&&this.#_(...e)},this.#v())},this.#_=(...e)=>{this.#x()&&(this.fn(...e),this.#b({executionCount:this.store.state.executionCount+1,isPending:!1,lastArgs:void 0}),this.options.onExecute?.(e,this))},this.flush=()=>{this.store.state.isPending&&this.store.state.lastArgs&&(this.#y(),this.#_(...this.store.state.lastArgs))},this.#y=()=>{this.#f&&(clearTimeout(this.#f),this.#f=void 0)},this.cancel=()=>{this.#y(),this.#b({canLeadingExecute:!0,isPending:!1})},this.reset=()=>{this.#b(C())},this.key=t.key,this.options={...E,...t},this.#b(this.options.initialState??{}),this.key&&m.on("d-Debouncer",e=>{e.payload.key===this.key&&(this.#b(e.payload.store.state),this.setOptions(e.payload.options))})}#b;#x;#v;#_;#y};e.s(["useDebouncer",0,function(e,t,a=()=>({})){let r={...((0,i.useContext)(s)?.defaultOptions??{}).debouncer,...t},[o]=(0,i.useState)(()=>{let t=new S(e,r);return t.Subscribe=function(e){let i=l(t.store,e.selector,{compare:n});return"function"==typeof e.children?e.children(i):e.children},t});o.fn=e,o.setOptions(r),(0,i.useEffect)(()=>()=>{r.onUnmount?r.onUnmount(o):o.cancel()},[]);let d=l(o.store,a,{compare:n});return(0,i.useMemo)(()=>({...o,state:d}),[o,d])}],540626)},546467,e=>{"use strict";let t=(0,e.i(475254).default)("external-link",[["path",{d:"M15 3h6v6",key:"1q9fwt"}],["path",{d:"M10 14 21 3",key:"gplh6r"}],["path",{d:"M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6",key:"a6xqqp"}]]);e.s(["default",0,t])},778917,e=>{"use strict";var t=e.i(546467);e.s(["ExternalLink",()=>t.default])},306228,e=>{"use strict";let t=(0,e.i(475254).default)("link-2",[["path",{d:"M9 17H7A5 5 0 0 1 7 7h2",key:"8i5ue5"}],["path",{d:"M15 7h2a5 5 0 1 1 0 10h-2",key:"1b9ql8"}],["line",{x1:"8",x2:"16",y1:"12",y2:"12",key:"1jonct"}]]);e.s(["Link2",0,t],306228)},198458,e=>{"use strict";var t=e.i(655063),i=e.i(266027),s=e.i(271645),n=e.i(741466);e.s(["useResourceList",0,function(e){let{queryKey:a,fetchPage:r,serializeFilters:o,defaultSorting:l,defaultPageSize:d,enabled:u}=e,[c,p]=(0,s.useState)(l),[m,g]=(0,s.useState)({pageIndex:0,pageSize:d}),[h,f]=(0,s.useState)([]),[x,b]=(0,s.useState)(""),[v]=(0,t.useDebouncedValue)(x,{wait:n.DEBOUNCE_WAIT_MS}),_=(0,s.useMemo)(()=>{let e=c.map(e=>e.desc?`-${e.id}`:e.id).join(","),t=v.trim();return{page:m.pageIndex+1,page_size:m.pageSize,...""===e?{}:{sort:e},...""===t?{}:{q:t},...o(h)}},[c,m.pageIndex,m.pageSize,v,h,o]),y={queryKey:[...a,_],queryFn:({signal:e})=>r(_,e),enabled:u,placeholderData:e=>e},{data:j,isLoading:w,isPlaceholderData:k,isFetching:N,error:C,refetch:E}=(0,i.useQuery)(y),S=(0,s.useCallback)(()=>g(e=>({...e,pageIndex:0})),[]),$=(0,s.useCallback)(e=>{p(e),S()},[S]),T=(0,s.useCallback)(e=>{f(e),S()},[S]),I=(0,s.useCallback)(e=>{b(e),S()},[S]),L=(0,s.useCallback)(()=>{E()},[E]);return{rows:(0,s.useMemo)(()=>j?.data??[],[j]),rowCount:j?.meta.total_count??0,isLoading:w||k,isFetching:N,error:C,refetch:L,sorting:c,onSortingChange:$,pagination:m,onPaginationChange:g,columnFilters:h,onColumnFiltersChange:T,searchValue:x,onSearchChange:I}}])},641141,e=>{"use strict";var t=e.i(843476),i=e.i(135214),s=e.i(222038),n=e.i(782066),a=e.i(664659),r=e.i(344523),o=e.i(465261),l=e.i(292270),d=e.i(263488),u=e.i(581418),c=e.i(284614),p=e.i(618566),m=e.i(799676),g=e.i(337822),h=e.i(772436),f=e.i(922407),x=e.i(196631),b=e.i(271645);e.s(["default",0,({onLogout:e,variant:v="navbar",collapsed:_=!1})=>{let{userId:y,userEmail:j,userRoleLabel:w,loginMethod:k}=(0,i.default)(),N=(0,p.useRouter)(),[C,E]=(0,b.useState)(!1),S=j||y||"user",$=function(e,t){let i=e?.split("@")[0]?.trim();if(i){let e=i.replace(/[^a-zA-Z0-9]+/g," ").trim().split(/\s+/).filter(Boolean);if(e.length>=2)return`${e[0].charAt(0)}${e[1].charAt(0)}`.toUpperCase();if(1===e.length){let t=e[0];return t.length>=2?t.slice(0,2).toUpperCase():`${t.charAt(0)}`.toUpperCase()}}return t&&t.length>=2?t.slice(0,2).toUpperCase():t&&1===t.length?`${t.toUpperCase()}•`:"?"}(j,y),T=function(e){let t=0;for(let i=0;i<e.length;i+=1)t=e.charCodeAt(i)+((t<<5)-t);return Math.abs(t)%360}(S),I=(0,s.navAccountDisplayName)(j,y);return(0,t.jsxs)(g.Popover,{open:C,onOpenChange:E,children:["sidebar"===v?(0,t.jsxs)(g.PopoverTrigger,{render:(0,t.jsx)("button",{type:"button",className:(0,x.cn)("flex w-full items-center rounded-lg border border-transparent transition-colors hover:bg-sidebar-accent",_?"justify-center px-0 py-1":"gap-2.5 px-2 py-1.5 text-left"),"aria-label":`Account menu — ${w??"Unknown role"} — signed in as ${j||y||"unknown"}`,"aria-haspopup":"dialog",title:_?I:void 0}),children:[(0,t.jsx)(m.Avatar,{className:"size-[30px] shadow-inner ring-1 ring-black/5","aria-hidden":!0,children:(0,t.jsx)(m.AvatarFallback,{className:"font-semibold text-white",style:{backgroundColor:`hsl(${T} 46% 38%)`},children:$})}),!_&&(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("span",{className:"min-w-0 flex-1 leading-tight",children:[(0,t.jsx)("span",{className:"block truncate text-[13px] font-medium text-sidebar-foreground",children:I}),w&&(0,t.jsx)("span",{className:"block truncate text-[11px] text-muted-foreground",children:w})]}),(0,t.jsx)(r.ChevronsUpDown,{size:16,strokeWidth:1.75,className:"shrink-0 text-muted-foreground","aria-hidden":!0})]})]}):(0,t.jsxs)(g.PopoverTrigger,{render:(0,t.jsx)("button",{type:"button",className:"flex! max-w-[min(200px,34vw)] items-center gap-2 rounded-md! py-0.5! pl-1! pr-2! transition-colors hover:bg-accent!","aria-label":`Account menu — ${w??"Unknown role"} — signed in as ${j||y||"unknown"}`,"aria-haspopup":"dialog"}),children:[(0,t.jsx)(m.Avatar,{className:"shadow-inner ring-1 ring-black/5","aria-hidden":!0,children:(0,t.jsx)(m.AvatarFallback,{className:"font-semibold text-white",style:{backgroundColor:`hsl(${T} 46% 38%)`},children:$})}),(0,t.jsx)("span",{className:"hidden min-w-0 truncate text-left text-sm font-medium leading-none text-foreground md:inline",children:I}),(0,t.jsx)(a.ChevronDown,{className:"hidden size-2.5 shrink-0 text-muted-foreground md:inline","aria-hidden":!0})]}),(0,t.jsxs)(g.PopoverContent,{align:"sidebar"===v?"start":"end",side:"sidebar"===v?"top":"bottom",className:"w-auto gap-0 rounded-lg bg-card p-1 shadow-lg","data-testid":"user-dropdown-panel",children:[(0,t.jsxs)("div",{className:"flex w-full flex-col gap-2 p-3 text-sm",children:[(0,t.jsxs)("div",{className:"flex w-full items-center gap-2",children:[(0,t.jsx)(d.Mail,{className:"size-4"}),(0,t.jsx)("span",{className:"text-muted-foreground",children:j||"-"})]}),(0,t.jsx)(h.Separator,{className:"my-2"}),(0,t.jsxs)("div",{className:"flex w-full items-center justify-between gap-2",children:[(0,t.jsxs)("div",{className:"flex items-center gap-2",children:[(0,t.jsx)(c.User,{className:"size-4"}),(0,t.jsx)("span",{className:"text-muted-foreground",children:"User ID"})]}),(0,t.jsxs)("div",{className:"flex items-center gap-1",children:[(0,t.jsx)("span",{className:"max-w-[150px] truncate",title:y||"-",children:y||"-"}),(0,t.jsx)(f.default,{value:y,label:"Copy User ID"})]})]}),(0,t.jsxs)("div",{className:"flex w-full items-center justify-between gap-2",children:[(0,t.jsxs)("div",{className:"flex items-center gap-2",children:[(0,t.jsx)(u.ShieldCheck,{className:"size-4"}),(0,t.jsx)("span",{className:"text-muted-foreground",children:"Role"})]}),(0,t.jsx)("span",{children:w})]})]}),(0,t.jsx)(h.Separator,{}),"username_password"===k&&(0,t.jsxs)("button",{type:"button",onClick:()=>{E(!1),N.push((0,n.uiHref)("change-password"))},className:"flex w-full items-center gap-2 rounded-sm px-2 py-1.5 text-sm hover:bg-accent",children:[(0,t.jsx)(o.KeyRound,{className:"size-4"}),"Change Password"]}),(0,t.jsxs)("button",{type:"button",onClick:e,className:"flex w-full items-center gap-2 rounded-sm px-2 py-1.5 text-sm hover:bg-accent",children:[(0,t.jsx)(l.LogOut,{className:"size-4"}),"Logout"]})]})]})}])},853295,658140,e=>{"use strict";var t=e.i(843476),i=e.i(618566),s=e.i(755146),n=e.i(643531),a=e.i(344523),r=e.i(373264),o=e.i(271645),l=e.i(431703),d=e.i(602869);let u=(0,o.createContext)({mode:"ai-gateway",setMode:()=>{},plugins:[],activePlugin:null}),c="litellm_plugin_mode",p=(0,l.createApiClient)({getBaseUrl:()=>(0,d.getProxyBaseUrl)()??""});function m(){return localStorage.getItem(c)??"ai-gateway"}function g(){return(0,o.useContext)(u)}e.s(["PluginModeProvider",0,function({children:e,accessToken:i}){let[s,n]=(0,o.useState)(m),[a,r]=(0,o.useState)([]),[l,d]=(0,o.useState)(!1);(0,o.useEffect)(()=>{if(!i)return;let e=!1;return p.get("/api/plugins",{accessToken:i}).then(t=>{e||r(Array.isArray(t)?t:[])}).catch(()=>{}).finally(()=>{e||d(!0)}),()=>{e=!0}},[i]);let g="ai-gateway"!==s&&l&&!a.some(e=>e.name===s)?"ai-gateway":s,h=a.find(e=>e.name===g)??null;return(0,t.jsx)(u.Provider,{value:{mode:g,setMode:e=>{n(e),localStorage.setItem(c,e)},plugins:a,activePlugin:h},children:e})},"usePluginMode",0,g],658140);var h=e.i(292639),f=e.i(782066);let x="chat";e.s(["default",0,function(){let{mode:e,setMode:o,plugins:l}=g(),{data:d}=(0,h.useUISettings)(),u=(0,i.usePathname)(),c=!!d?.values?.enable_chat_ui,p=(0,f.uiHref)(x),m=(u??"").replace(/\/+$/,""),b=c&&(m===p||m.startsWith(`${p}/`)),v=b?"Chat":l.find(t=>t.name===e)?.display_name??"AI Gateway",_=[{key:"ai-gateway",label:"AI Gateway"},...l.map(e=>({key:e.name,label:e.display_name}))],y=c?{key:x,label:(0,t.jsxs)("div",{className:"flex items-center justify-between gap-6 py-0.5",children:[(0,t.jsx)("span",{className:"font-medium",children:"Chat"}),b&&(0,t.jsx)(n.Check,{className:"size-4 text-info"})]}),onClick:()=>window.location.assign((0,f.uiHref)(x))}:{key:x,disabled:!0,label:(0,t.jsxs)("div",{className:"flex max-w-[220px] flex-col py-0.5",children:[(0,t.jsx)("span",{className:"font-medium",children:"Chat"}),(0,t.jsx)("span",{className:"whitespace-normal text-xs leading-snug text-muted-foreground",children:"Admins can enable in Settings"})]})},j=[..._.map(i=>({key:i.key,label:(0,t.jsxs)("div",{className:"flex items-center justify-between gap-6 py-0.5",children:[(0,t.jsx)("span",{className:"font-medium",children:i.label}),!b&&i.key===e&&(0,t.jsx)(n.Check,{className:"size-4 text-info"})]}),onClick:()=>{o(i.key),b&&window.location.assign((0,f.uiHref)(""))}})),y];return(0,t.jsxs)(s.DropdownMenu,{children:[(0,t.jsxs)(s.DropdownMenuTrigger,{render:(0,t.jsx)("button",{type:"button",className:"flex h-8 max-w-[220px] items-center gap-1.5 rounded-md border border-border bg-background pl-1.5 pr-2 text-sm font-medium text-foreground transition-colors hover:bg-accent"}),children:[(0,t.jsx)("span",{className:"flex size-5 flex-none items-center justify-center rounded bg-muted text-muted-foreground",children:(0,t.jsx)(r.LayoutGrid,{className:"size-[13px]"})}),(0,t.jsx)("span",{className:"truncate",children:v}),(0,t.jsx)(a.ChevronsUpDown,{className:"size-3.5 flex-none text-muted-foreground"})]}),(0,t.jsx)(s.DropdownMenuContent,{className:"w-auto",children:j.map(e=>(0,t.jsx)(s.DropdownMenuItem,{disabled:e.disabled,onClick:e.onClick,children:e.label},e.key))})]})}],853295)},383862,e=>{"use strict";var t=e.i(843476),i=e.i(618393),s=e.i(131792),n=e.i(950594),a=e.i(283713);e.s(["default",0,({onWorkerSwitch:e})=>{let{isControlPlane:r,selectedWorker:o,workers:l}=(0,a.useWorker)();if(!r||!o)return null;let d=l.map(e=>({label:e.name,value:e.worker_id,disabled:e.worker_id===o.worker_id}));return(0,t.jsxs)(s.Combobox,{items:d,value:d.find(e=>e.value===o.worker_id)??null,itemToStringLabel:e=>e.label,onValueChange:t=>{t&&e(t.value)},children:[(0,t.jsx)(s.ComboboxInput,{className:"min-w-[180px]","aria-label":"Worker",children:(0,t.jsx)(n.InputGroupAddon,{align:"inline-start",children:(0,t.jsx)(i.Server,{className:"size-4"})})}),(0,t.jsxs)(s.ComboboxContent,{children:[(0,t.jsx)(s.ComboboxEmpty,{children:"No matching workers"}),(0,t.jsx)(s.ComboboxList,{children:e=>(0,t.jsx)(s.ComboboxItem,{value:e,disabled:e.disabled,children:e.label},e.value)})]})]})}])},455880,e=>{"use strict";var t=e.i(843476),i=e.i(475254);let s=(0,i.default)("moon",[["path",{d:"M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z",key:"a7tn18"}]]),n=(0,i.default)("sun",[["circle",{cx:"12",cy:"12",r:"4",key:"4exip2"}],["path",{d:"M12 2v2",key:"tus03m"}],["path",{d:"M12 20v2",key:"1lh1kg"}],["path",{d:"m4.93 4.93 1.41 1.41",key:"149t6j"}],["path",{d:"m17.66 17.66 1.41 1.41",key:"ptbguv"}],["path",{d:"M2 12h2",key:"1t8f8n"}],["path",{d:"M20 12h2",key:"1q8mjw"}],["path",{d:"m6.34 17.66-1.41 1.41",key:"1m8zz5"}],["path",{d:"m19.07 4.93-1.41 1.41",key:"1shlcs"}]]);var a=e.i(363178),r=e.i(519455);e.s(["default",0,()=>{let{setTheme:e,resolvedTheme:i}=(0,a.useTheme)(),o="dark"===i,l=o?"Switch to light mode":"Switch to dark mode";return(0,t.jsx)(r.Button,{variant:"ghost",size:"icon-sm","aria-label":l,title:l,className:"text-muted-foreground",onClick:()=>e(o?"light":"dark"),children:o?(0,t.jsx)(s,{}):(0,t.jsx)(n,{})})}],455880)},909947,e=>{"use strict";var t=e.i(865361);e.s(["generateCodeSnippet",0,e=>{let i,{apiKeySource:s,accessToken:n,apiKey:a,inputMessage:r,chatHistory:o,selectedTags:l,selectedVectorStores:d,selectedGuardrails:u,selectedPolicies:c,selectedVoice:p,endpointType:m,selectedModel:g,selectedSdk:h,proxySettings:f,customHeaders:x}=e,b="session"===s?n:a,v=window.location.origin,_=f?.LITELLM_UI_API_DOC_BASE_URL;_&&_.trim()?v=_:f?.PROXY_BASE_URL&&(v=f.PROXY_BASE_URL);let y=r||"Your prompt here",j=y.replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n"),w=o.filter(e=>!e.isImage).map(({role:e,content:t})=>({role:e,content:t})),k={};l.length>0&&(k.tags=l),d.length>0&&(k.vector_stores=d),u.length>0&&(k.guardrails=u),c.length>0&&(k.policies=c);let N=g||"your-model-name",C=x&&Object.keys(x).length>0?`,
	default_headers=${JSON.stringify(x,null,2).replace(/\n/g,"\n	")}`:"",E="azure"===h?`import openai

client = openai.AzureOpenAI(
	api_key="${b||"YOUR_LITELLM_API_KEY"}",
	azure_endpoint="${v}",
	api_version="2024-02-01"${C}
)`:`import openai

client = openai.OpenAI(
	api_key="${b||"YOUR_LITELLM_API_KEY"}",
	base_url="${v}"${C}
)`;switch(m){case t.EndpointType.CHAT:{let e=Object.keys(k).length>0,t="";if(e){let e=JSON.stringify({metadata:k},null,2).split("\n").map(e=>" ".repeat(4)+e).join("\n").trim();t=`,
    extra_body=${e}`}let s=w.length>0?w:[{role:"user",content:y}];i=`
import base64

# Helper function to encode images to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Example with text only
response = client.chat.completions.create(
    model="${N}",
    messages=${JSON.stringify(s,null,4)}${t}
)

print(response)

# Example with image or PDF (uncomment and provide file path to use)
# base64_file = encode_image("path/to/your/file.jpg")  # or .pdf
# response_with_file = client.chat.completions.create(
#     model="${N}",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "${j}"
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{base64_file}"  # or data:application/pdf;base64,{base64_file}
#                     }
#                 }
#             ]
#         }
#     ]${t}
# )
# print(response_with_file)
`;break}case t.EndpointType.RESPONSES:{let e=Object.keys(k).length>0,t="";if(e){let e=JSON.stringify({metadata:k},null,2).split("\n").map(e=>" ".repeat(4)+e).join("\n").trim();t=`,
    extra_body=${e}`}let s=w.length>0?w:[{role:"user",content:y}];i=`
import base64

# Helper function to encode images to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Example with text only
response = client.responses.create(
    model="${N}",
    input=${JSON.stringify(s,null,4)}${t}
)

print(response.output_text)

# Example with image or PDF (uncomment and provide file path to use)
# base64_file = encode_image("path/to/your/file.jpg")  # or .pdf
# response_with_file = client.responses.create(
#     model="${N}",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "input_text", "text": "${j}"},
#                 {
#                     "type": "input_image",
#                     "image_url": f"data:image/jpeg;base64,{base64_file}",  # or data:application/pdf;base64,{base64_file}
#                 },
#             ],
#         }
#     ]${t}
# )
# print(response_with_file.output_text)
`;break}case t.EndpointType.IMAGE:i="azure"===h?`
# NOTE: The Azure SDK does not have a direct equivalent to the multi-modal 'responses.create' method shown for OpenAI.
# This snippet uses 'client.images.generate' and will create a new image based on your prompt.
# It does not use the uploaded image, as 'client.images.generate' does not support image inputs in this context.
import os
import requests
import json
import time
from PIL import Image

result = client.images.generate(
	model="${N}",
	prompt="${r}",
	n=1
)

json_response = json.loads(result.model_dump_json())

# Set the directory for the stored image
image_dir = os.path.join(os.curdir, 'images')

# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
	os.mkdir(image_dir)

# Initialize the image path
image_filename = f"generated_image_{int(time.time())}.png"
image_path = os.path.join(image_dir, image_filename)

try:
	# Retrieve the generated image
	if json_response.get("data") && len(json_response["data"]) > 0 && json_response["data"][0].get("url"):
			image_url = json_response["data"][0]["url"]
			generated_image = requests.get(image_url).content
			with open(image_path, "wb") as image_file:
					image_file.write(generated_image)

			print(f"Image saved to {image_path}")
			# Display the image
			image = Image.open(image_path)
			image.show()
	else:
			print("Could not find image URL in response.")
			print("Full response:", json_response)
except Exception as e:
	print(f"An error occurred: {e}")
	print("Full response:", json_response)
`:`
import base64
import os
import time
import json
from PIL import Image
import requests

# Helper function to encode images to base64
def encode_image(image_path):
	with open(image_path, "rb") as image_file:
			return base64.b64encode(image_file.read()).decode('utf-8')

# Helper function to create a file (simplified for this example)
def create_file(image_path):
	# In a real implementation, this would upload the file to OpenAI
	# For this example, we'll just return a placeholder ID
	return f"file_{os.path.basename(image_path).replace('.', '_')}"

# The prompt entered by the user
prompt = "${j}"

# Encode images to base64
base64_image1 = encode_image("body-lotion.png")
base64_image2 = encode_image("soap.png")

# Create file IDs
file_id1 = create_file("body-lotion.png")
file_id2 = create_file("incense-kit.png")

response = client.responses.create(
	model="${N}",
	input=[
			{
					"role": "user",
					"content": [
							{"type": "input_text", "text": prompt},
							{
									"type": "input_image",
									"image_url": f"data:image/jpeg;base64,{base64_image1}",
							},
							{
									"type": "input_image",
									"image_url": f"data:image/jpeg;base64,{base64_image2}",
							},
							{
									"type": "input_image",
									"file_id": file_id1,
							},
							{
									"type": "input_image",
									"file_id": file_id2,
							}
					],
			}
	],
	tools=[{"type": "image_generation"}],
)

# Process the response
image_generation_calls = [
	output
	for output in response.output
	if output.type == "image_generation_call"
]

image_data = [output.result for output in image_generation_calls]

if image_data:
	image_base64 = image_data[0]
	image_filename = f"edited_image_{int(time.time())}.png"
	with open(image_filename, "wb") as f:
			f.write(base64.b64decode(image_base64))
	print(f"Image saved to {image_filename}")
else:
	# If no image is generated, there might be a text response with an explanation
	text_response = [output.text for output in response.output if hasattr(output, 'text')]
	if text_response:
			print("No image generated. Model response:")
			print("\\n".join(text_response))
	else:
			print("No image data found in response.")
	print("Full response for debugging:")
	print(response)
`;break;case t.EndpointType.IMAGE_EDITS:i="azure"===h?`
import base64
import os
import time
import json
from PIL import Image
import requests

# Helper function to encode images to base64
def encode_image(image_path):
	with open(image_path, "rb") as image_file:
			return base64.b64encode(image_file.read()).decode('utf-8')

# The prompt entered by the user
prompt = "${j}"

# Encode images to base64
base64_image1 = encode_image("body-lotion.png")
base64_image2 = encode_image("soap.png")

# Create file IDs
file_id1 = create_file("body-lotion.png")
file_id2 = create_file("incense-kit.png")

response = client.responses.create(
	model="${N}",
	input=[
			{
					"role": "user",
					"content": [
							{"type": "input_text", "text": prompt},
							{
									"type": "input_image",
									"image_url": f"data:image/jpeg;base64,{base64_image1}",
							},
							{
									"type": "input_image",
									"image_url": f"data:image/jpeg;base64,{base64_image2}",
							},
							{
									"type": "input_image",
									"file_id": file_id1,
							},
							{
									"type": "input_image",
									"file_id": file_id2,
							}
					],
			}
	],
	tools=[{"type": "image_generation"}],
)

# Process the response
image_generation_calls = [
	output
	for output in response.output
	if output.type == "image_generation_call"
]

image_data = [output.result for output in image_generation_calls]

if image_data:
	image_base64 = image_data[0]
	image_filename = f"edited_image_{int(time.time())}.png"
	with open(image_filename, "wb") as f:
			f.write(base64.b64decode(image_base64))
	print(f"Image saved to {image_filename}")
else:
	# If no image is generated, there might be a text response with an explanation
	text_response = [output.text for output in response.output if hasattr(output, 'text')]
	if text_response:
			print("No image generated. Model response:")
			print("\\n".join(text_response))
	else:
			print("No image data found in response.")
	print("Full response for debugging:")
	print(response)
`:`
import base64
import os
import time

# Helper function to encode images to base64
def encode_image(image_path):
	with open(image_path, "rb") as image_file:
			return base64.b64encode(image_file.read()).decode('utf-8')

# Helper function to create a file (simplified for this example)
def create_file(image_path):
	# In a real implementation, this would upload the file to OpenAI
	# For this example, we'll just return a placeholder ID
	return f"file_{os.path.basename(image_path).replace('.', '_')}"

# The prompt entered by the user
prompt = "${j}"

# Encode images to base64
base64_image1 = encode_image("body-lotion.png")
base64_image2 = encode_image("soap.png")

# Create file IDs
file_id1 = create_file("body-lotion.png")
file_id2 = create_file("incense-kit.png")

response = client.responses.create(
	model="${N}",
	input=[
			{
					"role": "user",
					"content": [
							{"type": "input_text", "text": prompt},
							{
									"type": "input_image",
									"image_url": f"data:image/jpeg;base64,{base64_image1}",
							},
							{
									"type": "input_image",
									"image_url": f"data:image/jpeg;base64,{base64_image2}",
							},
							{
									"type": "input_image",
									"file_id": file_id1,
							},
							{
									"type": "input_image",
									"file_id": file_id2,
							}
					],
			}
	],
	tools=[{"type": "image_generation"}],
)

# Process the response
image_generation_calls = [
	output
	for output in response.output
	if output.type == "image_generation_call"
]

image_data = [output.result for output in image_generation_calls]

if image_data:
	image_base64 = image_data[0]
	image_filename = f"edited_image_{int(time.time())}.png"
	with open(image_filename, "wb") as f:
			f.write(base64.b64decode(image_base64))
	print(f"Image saved to {image_filename}")
else:
	# If no image is generated, there might be a text response with an explanation
	text_response = [output.text for output in response.output if hasattr(output, 'text')]
	if text_response:
			print("No image generated. Model response:")
			print("\\n".join(text_response))
	else:
			print("No image data found in response.")
	print("Full response for debugging:")
	print(response)
`;break;case t.EndpointType.EMBEDDINGS:i=`
response = client.embeddings.create(
	input="${r||"Your string here"}",
	model="${N}",
	encoding_format="base64" # or "float"
)

print(response.data[0].embedding)
`;break;case t.EndpointType.TRANSCRIPTION:i=`
# Open the audio file
audio_file = open("path/to/your/audio/file.mp3", "rb")

# Make the transcription request
response = client.audio.transcriptions.create(
	model="${N}",
	file=audio_file${r?`,
	prompt="${r.replace(/\\/g,"\\\\").replace(/"/g,'\\"')}"`:""}
)

print(response.text)
`;break;case t.EndpointType.SPEECH:i=`
# Make the text-to-speech request
response = client.audio.speech.create(
	model="${N}",
	input="${r||"Your text to convert to speech here"}",
	voice="${p}"  # Options: alloy, ash, ballad, coral, echo, fable, nova, onyx, sage, shimmer
)

# Save the audio to a file
output_filename = "output_speech.mp3"
response.stream_to_file(output_filename)
print(f"Audio saved to {output_filename}")

# Optional: Customize response format and speed
# response = client.audio.speech.create(
#     model="${N}",
#     input="${r||"Your text to convert to speech here"}",
#     voice="alloy",
#     response_format="mp3",  # Options: mp3, opus, aac, flac, wav, pcm
#     speed=1.0  # Range: 0.25 to 4.0
# )
# response.stream_to_file("output_speech.mp3")
`;break;default:i="\n# Code generation for this endpoint is not implemented yet."}return`${E}
${i}`}])},652272,209261,e=>{"use strict";var t=e.i(843476),i=e.i(271645),s=e.i(871689),n=e.i(643531),a=e.i(174886),r=e.i(306228),o=e.i(196631);let l=/^[a-zA-Z0-9][a-zA-Z0-9._-]*(\/[a-zA-Z0-9][a-zA-Z0-9._-]*)*$/,d=e=>e.trim().replace(/\/+$/,""),u=/\.(md|markdown|txt|json|ya?ml|toml)$/i,c=/\.zip$/i,p=/^[0-9a-fA-F]{64}$/,m=/^\d{1,3}(\.\d{1,3}){3}$/,g=/^[A-Za-z0-9-]+$/,h=/^[A-Za-z0-9._-]+$/,f=/^https?:\/\//i,x="ssh://",b=/^([a-z0-9._-]+)@([^:/@]+):(?!\/)(.+)$/i,v=e=>e.pathname.split("/").filter(e=>""!==e),_=e=>{try{return new URL(e)}catch{return null}},y=e=>e.hostname.includes(".")&&!e.hostname.startsWith("[")&&!m.test(e.hostname),j=e=>{let t=e.split("/").filter(e=>""!==e);return t[t.length-1]??""},w=e=>e.toLowerCase().replace(/[^a-z0-9-]+/g,"-").replace(/-+/g,"-").replace(/^-+|-+$/g,""),k=(e,t,i,s)=>{let n=d(s??"");return""!==n?l.test(n)?{parsed:{source:"git-subdir",url:t,path:n},label:`${e} subdir — ${t} @ ${n}`,suggestedName:w(j(n))}:null:{parsed:{source:"url",url:t},label:`${e} repo — ${t}`,suggestedName:w(i)}},N=e=>JSON.stringify({extraKnownMarketplaces:{litellm:{source:{source:"url",url:`${e}/claude-code/marketplace.json`}}}},null,2),C=e=>`/plugin install ${e.name}@litellm`,E=e=>"github"===e.source&&e.repo?`GitHub: ${e.repo}`:"git-subdir"===e.source&&e.url&&e.path?`${e.url} @ ${e.path}`:("url"===e.source||"archive"===e.source)&&e.url?e.url:"Unknown source",S=e=>"github"===e.source&&e.repo?`https://github.com/${e.repo}`:("url"===e.source||"git-subdir"===e.source||"archive"===e.source)&&e.url&&f.test(e.url)?e.url:null;e.s(["buildMarketplaceSettingsSnippet",0,N,"formatInstallCommand",0,C,"getCategoryBadgeColor",0,e=>{if(!e)return"gray";let t=e.toLowerCase();if(t.includes("development")||t.includes("dev"))return"blue";if(t.includes("productivity")||t.includes("workflow"))return"green";if(t.includes("learning")||t.includes("education"))return"purple";if(t.includes("security")||t.includes("safety"))return"red";if(t.includes("data")||t.includes("analytics"))return"orange";else if(t.includes("integration")||t.includes("api"))return"yellow";return"gray"},"getSourceDisplayText",0,E,"getSourceLink",0,S,"isValidEmail",0,e=>!e||/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e),"isValidSemanticVersion",0,e=>!e||/^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?(\+[a-zA-Z0-9.-]+)?$/.test(e),"isValidSha256",0,e=>""===e.trim()||p.test(e.trim()),"isValidSubPath",0,e=>{let t=d(e);return""!==t&&l.test(t)},"parseKeywords",0,e=>e&&""!==e.trim()?e.split(",").map(e=>e.trim()).filter(e=>""!==e):[],"parseSkillSource",0,(e,t)=>{let i=((e,t)=>{let i=e.trim(),s=b.exec(i),n=s?`${x}${s[1]}@${s[2]}/${s[3]}`:i;if(!n.toLowerCase().startsWith(x))return null;let a=_(n);if(!a||""===a.username||""!==a.password||!y(a))return null;let r=n.indexOf("/",x.length);return -1===r||a.pathname!==n.slice(r)||v(a).length<2?null:k("SSH",i,j(a.pathname).replace(/\.git$/i,""),t)})(e,t);if(i)return i;let s=(e=>{let t=e.trim();if(""===t||t.startsWith("//"))return null;let i=_(/^[a-z][a-z0-9+.-]*:\/\//i.test(t)?t:`https://${t}`);return i&&"https:"===i.protocol&&""===i.username&&""===i.password&&y(i)?i:null})(e);if(!s)return null;if(c.test(s.pathname))return{parsed:{source:"archive",url:s.href},label:`Zip archive — ${s.host}${s.pathname}`,suggestedName:w(j(s.pathname).replace(c,""))};if("github.com"===s.hostname.replace(/^www\./,""))return((e,t)=>{let i=v(e);if(i.length<2)return null;let s=i[0],n=i[1].replace(/\.git$/,"");if(!g.test(s)||!h.test(n))return null;let a=`${s}/${n}`,r=`https://github.com/${a}`,o={parsed:{source:"github",repo:a},label:`GitHub repo — ${a}`,suggestedName:w(n)};if(i.length>=4&&("tree"===i[2]||"blob"===i[2])){let e=i.slice(4),t=j(e.join("/")),s=u.test(t)?e.slice(0,-1):e;if(0===s.length)return o;let n=d(s.join("/"));return l.test(n)?{parsed:{source:"git-subdir",url:r,path:n},label:`GitHub subdir — ${a} @ ${n}`,suggestedName:w(j(n))}:null}if(2!==i.length)return null;let c=d(t??"");return""!==c?l.test(c)?{parsed:{source:"git-subdir",url:r,path:c},label:`GitHub subdir — ${a} @ ${c}`,suggestedName:w(j(c))}:null:o})(s,t);if(v(s).length<2)return null;let n=j(s.pathname).replace(/\.git$/,"");return k("Git",`${s.protocol}//${s.host}${s.pathname.replace(/\/+$/,"")}`,n,t)},"validatePluginName",0,e=>!!e&&""!==e.trim()&&/^[a-z0-9-]+$/.test(e)],209261);let $=({source:e})=>{let i=S(e),s=i&&"git-subdir"===e.source&&e.path?`${i}/tree/main/${e.path}`:i;return s?(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Source"}),(0,t.jsxs)("a",{href:s,target:"_blank",rel:"noopener noreferrer",className:"flex items-center gap-1 break-all text-[13px] text-info",children:[s.replace("https://",""),(0,t.jsx)(r.Link2,{className:"size-3 shrink-0"})]})]}):e.url?(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Source"}),(0,t.jsx)("div",{className:"break-all text-[13px] text-foreground",children:E(e)})]}):null};e.s(["default",0,({skill:e,onBack:r})=>{let[l,d]=(0,i.useState)("overview"),[u,c]=(0,i.useState)(null),p=(e,t)=>{navigator.clipboard.writeText(e),c(t),setTimeout(()=>c(null),2e3)},m=C(e),g=N(window.location.origin),h=[...e.category?[{property:"Category",value:e.category}]:[],...e.domain?[{property:"Domain",value:e.domain}]:[],...e.namespace?[{property:"Namespace",value:e.namespace}]:[],...e.version?[{property:"Version",value:e.version}]:[],...e.author?.name?[{property:"Author",value:e.author.name}]:[],...e.created_at?[{property:"Added",value:new Date(e.created_at).toLocaleDateString()}]:[]];return(0,t.jsxs)("div",{className:"py-6 pl-0 pr-8",children:[(0,t.jsxs)("div",{onClick:r,className:"mb-6 inline-flex cursor-pointer items-center gap-1.5 text-sm text-muted-foreground",children:[(0,t.jsx)(s.ArrowLeft,{className:"size-3"}),(0,t.jsx)("span",{children:"Skills"})]}),(0,t.jsxs)("div",{className:"mb-2",children:[(0,t.jsx)("h1",{className:"m-0 text-[28px] font-normal leading-tight text-foreground",children:e.name}),e.description&&(0,t.jsx)("p",{className:"mb-0 ml-0 mr-0 mt-2 text-sm leading-relaxed text-muted-foreground",children:e.description})]}),(0,t.jsx)("div",{className:"mb-7 mt-6 border-b border-border",children:(0,t.jsx)("div",{className:"flex",children:[{key:"overview",label:"Overview"},{key:"usage",label:"How to Use"}].map(e=>(0,t.jsx)("div",{onClick:()=>d(e.key),className:(0,o.cn)("-mb-px cursor-pointer border-b-[3px] px-5 py-3 text-sm",l===e.key?"border-info font-medium text-info":"border-transparent font-normal text-muted-foreground"),children:e.label},e.key))})}),"overview"===l&&(0,t.jsxs)("div",{className:"flex gap-16",children:[(0,t.jsxs)("div",{className:"min-w-0 flex-1",children:[(0,t.jsx)("h2",{className:"m-0 mb-1 text-lg font-normal text-foreground",children:"Skill Details"}),(0,t.jsx)("p",{className:"m-0 mb-4 text-[13px] text-muted-foreground",children:"Metadata registered with this skill"}),(0,t.jsxs)("table",{className:"w-full border-collapse text-sm",children:[(0,t.jsx)("thead",{children:(0,t.jsxs)("tr",{className:"border-b border-border",children:[(0,t.jsx)("th",{className:"w-40 py-3 text-left font-medium text-muted-foreground",children:"Property"}),(0,t.jsx)("th",{className:"py-3 text-left font-medium text-muted-foreground",children:e.name})]})}),(0,t.jsx)("tbody",{children:h.map((e,i)=>(0,t.jsxs)("tr",{className:"border-b border-border",children:[(0,t.jsx)("td",{className:"py-3 text-foreground",children:e.property}),(0,t.jsx)("td",{className:"py-3 text-foreground",children:e.value})]},i))})]})]}),(0,t.jsxs)("div",{className:"w-60 shrink-0",children:[(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Status"}),(0,t.jsx)("span",{className:(0,o.cn)("rounded-xl px-2.5 py-[3px] text-xs font-medium",e.enabled?"bg-success/10 text-success":"bg-muted text-muted-foreground"),children:e.enabled?"Public":"Draft"})]}),(0,t.jsx)($,{source:e.source}),e.keywords&&e.keywords.length>0&&(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-2 text-xs text-muted-foreground",children:"Tags"}),(0,t.jsx)("div",{className:"flex flex-wrap gap-1.5",children:e.keywords.map(e=>(0,t.jsx)("span",{className:"rounded-2xl border border-border bg-card px-3 py-1 text-xs text-foreground",children:e},e))})]}),(0,t.jsxs)("div",{children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Skill ID"}),(0,t.jsx)("div",{className:"break-all font-mono text-xs text-foreground",children:e.id})]})]})]}),"usage"===l&&(0,t.jsxs)("div",{className:"max-w-[640px]",children:[(0,t.jsx)("h2",{className:"m-0 mb-2 text-lg font-normal text-foreground",children:"Using this skill"}),(0,t.jsx)("p",{className:"m-0 mb-6 text-sm leading-relaxed text-muted-foreground",children:"Once your proxy is set as a marketplace, enable this skill in Claude Code with one command:"}),(0,t.jsxs)("div",{className:"mb-6 overflow-hidden rounded-lg border border-border",children:[(0,t.jsxs)("div",{className:"flex items-center justify-between border-b border-border bg-muted px-4 py-2.5",children:[(0,t.jsx)("span",{className:"text-[13px] font-medium text-foreground",children:"Run in Claude Code"}),(0,t.jsxs)("button",{onClick:()=>p(m,"install"),className:(0,o.cn)("flex cursor-pointer items-center gap-1 border-none bg-transparent p-0 text-xs","install"===u?"text-success":"text-info"),children:["install"===u?(0,t.jsx)(n.Check,{className:"size-3"}):(0,t.jsx)(a.Copy,{className:"size-3"}),"install"===u?"Copied":"Copy"]})]}),(0,t.jsx)("pre",{className:"m-0 bg-card px-4 py-3.5 font-mono text-sm text-foreground",children:m})]}),(0,t.jsxs)("div",{className:"mb-4 rounded-lg border border-warning/30 bg-warning/10 px-4 py-3",children:[(0,t.jsxs)("p",{className:"m-0 mb-2 text-[13px] leading-relaxed text-muted-foreground",children:['If you see "Plugin ',e.name,' not found in marketplace", update the catalog first:']}),(0,t.jsx)("pre",{className:"m-0 bg-transparent font-mono text-[13px] text-foreground",children:"/plugin marketplace update litellm"})]}),(0,t.jsxs)("p",{className:"m-0 text-[13px] leading-relaxed text-muted-foreground",children:["Don't have the marketplace configured yet?"," ",(0,t.jsx)("span",{onClick:()=>d("setup"),className:"cursor-pointer text-info",children:"See one-time setup →"})]})]}),"setup"===l&&(0,t.jsxs)("div",{className:"max-w-[640px]",children:[(0,t.jsx)("h2",{className:"m-0 mb-2 text-lg font-normal text-foreground",children:"One-time marketplace setup"}),(0,t.jsx)("p",{className:"m-0 mb-3 text-sm leading-relaxed text-muted-foreground",children:"Run this command in Claude Code to register the marketplace:"}),(0,t.jsxs)("div",{className:"mb-6 overflow-hidden rounded-lg border border-border",children:[(0,t.jsxs)("div",{className:"flex items-center justify-between border-b border-border bg-muted px-4 py-2.5",children:[(0,t.jsx)("span",{className:"text-[13px] font-medium text-foreground",children:"Run in Claude Code"}),(0,t.jsxs)("button",{onClick:()=>{let e=window.location.origin;p(`/plugin marketplace add ${e}/claude-code/marketplace.json`,"marketplace-cmd")},className:(0,o.cn)("flex cursor-pointer items-center gap-1 border-none bg-transparent p-0 text-xs","marketplace-cmd"===u?"text-success":"text-info"),children:["marketplace-cmd"===u?(0,t.jsx)(n.Check,{className:"size-3"}):(0,t.jsx)(a.Copy,{className:"size-3"}),"marketplace-cmd"===u?"Copied":"Copy"]})]}),(0,t.jsx)("pre",{className:"m-0 bg-card px-4 py-3.5 font-mono text-[13px] text-foreground",children:`/plugin marketplace add ${window.location.origin}/claude-code/marketplace.json`})]}),(0,t.jsxs)("p",{className:"m-0 mb-3 text-sm leading-relaxed text-muted-foreground",children:["Or add this to ",(0,t.jsx)("code",{className:"rounded bg-muted px-1.5 py-px text-[13px]",children:"~/.claude/settings.json"})," ","for a persistent configuration:"]}),(0,t.jsxs)("div",{className:"overflow-hidden rounded-lg border border-border",children:[(0,t.jsxs)("div",{className:"flex items-center justify-between border-b border-border bg-muted px-4 py-2.5",children:[(0,t.jsx)("span",{className:"text-[13px] font-medium text-foreground",children:"~/.claude/settings.json"}),(0,t.jsxs)("button",{onClick:()=>p(g,"settings"),className:(0,o.cn)("flex cursor-pointer items-center gap-1 border-none bg-transparent p-0 text-xs","settings"===u?"text-success":"text-info"),children:["settings"===u?(0,t.jsx)(n.Check,{className:"size-3"}):(0,t.jsx)(a.Copy,{className:"size-3"}),"settings"===u?"Copied":"Copy"]})]}),(0,t.jsx)("pre",{className:"m-0 bg-card px-4 py-3.5 font-mono text-[13px] text-foreground",children:g})]})]})]})}],652272)},402874,e=>{"use strict";var t=e.i(843476),i=e.i(283713),s=e.i(602869),n=e.i(782066),a=e.i(275144),r=e.i(886400),o=e.i(321836),l=e.i(972518),d=e.i(799647),u=e.i(522016),c=e.i(196631),p=e.i(641141),m=e.i(455880),g=e.i(853295),h=e.i(383862);let f="h-auto max-h-full w-auto max-w-full object-contain";e.s(["default",0,({accessToken:e,isPublicPage:x=!1,sidebarCollapsed:b=!1,onToggleSidebar:v})=>{let _=(0,s.getProxyBaseUrl)(),{logoUrl:y}=(0,a.useTheme)(),{isControlPlane:j,selectedWorker:w}=(0,i.useWorker)(),k=y||`${_}/get_image`,N=y||`${_}/get_image?theme=dark`,C=(0,r.useLogout)(e);return(0,t.jsx)("nav",{className:"sticky top-0 z-chrome border-b border-border bg-card",children:(0,t.jsx)("div",{className:"w-full",children:(0,t.jsxs)("div",{className:"flex h-14 items-center px-4",children:[(0,t.jsxs)("div",{className:"flex shrink-0 items-center",children:[v&&(0,t.jsx)("button",{onClick:v,className:"mr-2 flex h-9 w-9 items-center justify-center rounded-md text-muted-foreground transition-colors hover:bg-accent hover:text-foreground",title:b?"Expand sidebar":"Collapse sidebar",children:(0,t.jsx)("span",{className:"text-lg",children:b?(0,t.jsx)(d.PanelLeftOpen,{className:"size-[18px]"}):(0,t.jsx)(l.PanelLeftClose,{className:"size-[18px]"})})}),(0,t.jsx)("div",{className:"flex items-center gap-2",children:(0,t.jsx)(u.default,{href:(0,n.uiHref)(""),className:"flex items-center",children:(0,t.jsx)("div",{className:"relative",children:(0,t.jsxs)("div",{className:"flex h-10 max-w-48 items-center justify-center overflow-hidden",children:[(0,t.jsx)("img",{src:k,alt:"EmbRouter Brand",className:(0,c.cn)(f,"dark:hidden")}),(0,t.jsx)("img",{src:N,alt:"","aria-hidden":!0,className:(0,c.cn)(f,"hidden dark:block")})]})})})})]}),!x&&(0,t.jsx)("div",{className:"ml-4 flex shrink-0 items-center border-l border-border pl-4",children:(0,t.jsx)(g.default,{})}),(0,t.jsxs)("div",{className:"ml-auto flex min-w-0 flex-1 items-center justify-end gap-4",children:[j&&null!==w&&(0,t.jsx)("div",{className:"flex shrink-0 items-center",children:(0,t.jsx)(h.default,{onWorkerSwitch:t=>{(0,r.revokeSessionAndClearClientState)(e).finally(()=>{window.location.href=`${(0,o.getLoginUrl)()}?worker=${encodeURIComponent(t)}`})}})}),!x&&(0,t.jsx)("div",{className:"flex shrink-0 items-center border-l border-border pl-4",children:(0,t.jsxs)("div",{className:"flex items-center gap-0.5 rounded-lg bg-muted px-1 py-0 transition-colors hover:bg-accent",children:[(0,t.jsx)(m.default,{}),(0,t.jsx)("span",{className:"mx-0.5 h-6 w-px shrink-0 bg-border","aria-hidden":!0}),(0,t.jsx)(p.default,{onLogout:C})]})})]})]})})})}])},845150,e=>{"use strict";var t=e.i(843476),i=e.i(271645),s=e.i(131792);let n=(e,t)=>{let i=t.trim().toLowerCase();return!i||e.label.toLowerCase().includes(i)||e.value.toLowerCase().includes(i)||(e.description?.toLowerCase().includes(i)??!1)};e.s(["MultiSelect",0,function({id:e,options:a,value:r=[],onValueChange:o,placeholder:l="Select options",emptyText:d="No options found",disabled:u=!1,loading:c=!1,allowCustomValues:p=!1,className:m}){let g=(0,s.useComboboxAnchor)(),[h,f]=(0,i.useState)(""),x=a.filter(e=>null!=e&&"string"==typeof e.value&&e.value.length>0),b=r.filter(e=>"string"==typeof e&&e.length>0).map(e=>x.find(t=>t.value===e)??{label:e,value:e}),v=h.trim(),_=x.some(e=>e.value.toLowerCase()===v.toLowerCase()),y=p&&v&&!_?[...x,{label:`Create "${v}"`,value:v}]:x;return(0,t.jsxs)(s.Combobox,{multiple:!0,items:y,value:b,onValueChange:e=>{o(Array.from(new Set(p?e.flatMap(e=>r.includes(e.value)?[e.value]:e.value.split(",").map(e=>e.trim()).filter(e=>e.length>0)):e.map(e=>e.value)))),f("")},inputValue:h,onInputValueChange:f,isItemEqualToValue:(e,t)=>e.value===t.value,itemToStringLabel:e=>e.label,filter:n,disabled:u||c,children:[(0,t.jsx)(s.ComboboxChips,{render:(0,t.jsx)("div",{ref:g}),className:`min-h-8 py-1 text-sm ${m??""}`,children:(0,t.jsx)(s.ComboboxValue,{children:i=>(0,t.jsxs)(t.Fragment,{children:[i.map(e=>(0,t.jsx)(s.ComboboxChip,{"aria-label":e.label,children:e.label},e.value)),(0,t.jsx)(s.ComboboxChipsInput,{id:e,placeholder:c?"Loading...":l,className:"min-w-24","aria-label":l||void 0}),i.length>0&&!u&&!c&&(0,t.jsx)(s.ComboboxClear,{className:"ml-auto self-center","aria-label":"Clear all"})]})})}),(0,t.jsxs)(s.ComboboxContent,{anchor:g,children:[(0,t.jsx)(s.ComboboxEmpty,{children:d}),(0,t.jsx)(s.ComboboxList,{children:e=>(0,t.jsx)(s.ComboboxItem,{value:e,disabled:e.disabled,children:(0,t.jsxs)("span",{className:"min-w-0",children:[(0,t.jsx)("span",{className:"block truncate",children:e.label}),e.description&&(0,t.jsx)("span",{className:"block truncate text-xs text-muted-foreground",children:e.description})]})},e.value)})]})]})}])},283713,e=>{"use strict";var t=e.i(271645),i=e.i(602869),s=e.i(612256);let n="litellm_selected_worker_id";e.s(["useWorker",0,()=>{let{data:e}=(0,s.useUIConfig)(),a=e?.is_control_plane??!1,r=e?.workers??[],[o,l]=(0,t.useState)(()=>localStorage.getItem(n));(0,t.useEffect)(()=>{if(!o||0===r.length)return;let e=r.find(e=>e.worker_id===o);e&&(0,i.switchToWorkerUrl)(e.url)},[o,r]);let d=r.find(e=>e.worker_id===o)??null,u=(0,t.useCallback)(e=>{let t=r.find(t=>t.worker_id===e);t&&(l(e),localStorage.setItem(n,e),(0,i.switchToWorkerUrl)(t.url))},[r]);return{isControlPlane:a,workers:r,selectedWorkerId:o,selectedWorker:d,selectWorker:u,disconnectFromWorker:(0,t.useCallback)(()=>{l(null),localStorage.removeItem(n),(0,i.switchToWorkerUrl)(null)},[])}}])},741466,e=>{"use strict";e.s(["DEBOUNCE_WAIT_MS",0,300])},899426,e=>{"use strict";let t=e=>e.trim().toLowerCase();function i(e,i){let s=t(e);if(""===s)return!0;let n=i.filter(e=>"string"==typeof e).map(e=>e.toLowerCase());return!!n.some(e=>e.includes(s))||s.split(/\s+/).every(e=>n.some(t=>t.includes(e)))}e.s(["filterBySearchTerm",0,function(e,t,s){return e.filter(e=>i(t,s(e)))},"matchesSearchTerm",0,i,"rankBySearchRelevance",0,function(e,i,s){let n=t(i);if(""===n)return[...e];let a=e=>{let t=s(e).toLowerCase();return 1e3*(t===n)+100*!!t.startsWith(n)+(1e3-t.length)};return[...e].sort((e,t)=>a(t)-a(e))}])}]);