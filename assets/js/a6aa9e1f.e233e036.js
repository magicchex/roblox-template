"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[89],{93269:(e,t,a)=>{a.r(t),a.d(t,{default:()=>k});var n=a(67294),l=a(86010),r=a(52263),i=a(1944),o=a(35281),s=a(39058),c=a(95999),m=a(32244);function g(e){const{metadata:t}=e,{previousPage:a,nextPage:l}=t;return n.createElement("nav",{className:"pagination-nav","aria-label":(0,c.I)({id:"theme.blog.paginator.navAriaLabel",message:"Blog list page navigation",description:"The ARIA label for the blog pagination"})},a&&n.createElement(m.Z,{permalink:a,title:n.createElement(c.Z,{id:"theme.blog.paginator.newerEntries",description:"The label used to navigate to the newer blog posts page (previous page)"},"Newer Entries")}),l&&n.createElement(m.Z,{permalink:l,title:n.createElement(c.Z,{id:"theme.blog.paginator.olderEntries",description:"The label used to navigate to the older blog posts page (next page)"},"Older Entries"),isNext:!0}))}var p=a(90197),d=a(9460),u=a(40756);function E(e){let{items:t,component:a=u.Z}=e;return n.createElement(n.Fragment,null,t.map((e=>{let{content:t}=e;return n.createElement(d.n,{key:t.metadata.permalink,content:t},n.createElement(a,null,n.createElement(t,null)))})))}function b(e){const{metadata:t}=e,{siteConfig:{title:a}}=(0,r.Z)(),{blogDescription:l,blogTitle:o,permalink:s}=t,c="/"===s?a:o;return n.createElement(n.Fragment,null,n.createElement(i.d,{title:c,description:l}),n.createElement(p.Z,{tag:"blog_posts_list"}))}function h(e){const{metadata:t,items:a,sidebar:l}=e;return n.createElement(s.Z,{sidebar:l},n.createElement(E,{items:a}),n.createElement(g,{metadata:t}))}function k(e){return n.createElement(i.FG,{className:(0,l.Z)(o.k.wrapper.blogPages,o.k.page.blogListPage)},n.createElement(b,e),n.createElement(h,e))}}}]);