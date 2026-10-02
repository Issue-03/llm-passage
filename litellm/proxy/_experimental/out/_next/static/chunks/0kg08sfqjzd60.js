(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,306228,e=>{"use strict";let t=(0,e.i(475254).default)("link-2",[["path",{d:"M9 17H7A5 5 0 0 1 7 7h2",key:"8i5ue5"}],["path",{d:"M15 7h2a5 5 0 1 1 0 10h-2",key:"1b9ql8"}],["line",{x1:"8",x2:"16",y1:"12",y2:"12",key:"1jonct"}]]);e.s(["Link2",0,t],306228)},641141,e=>{"use strict";var t=e.i(843476),a=e.i(135214),s=e.i(222038),r=e.i(782066),i=e.i(664659),n=e.i(344523),l=e.i(465261),o=e.i(292270),d=e.i(263488),m=e.i(581418),p=e.i(284614),c=e.i(618566),u=e.i(799676),g=e.i(337822),x=e.i(772436),h=e.i(922407),f=e.i(196631),b=e.i(271645);e.s(["default",0,({onLogout:e,variant:_="navbar",collapsed:j=!1})=>{let{userId:y,userEmail:w,userRoleLabel:N,loginMethod:k}=(0,a.default)(),v=(0,c.useRouter)(),[$,C]=(0,b.useState)(!1),S=w||y||"user",I=function(e,t){let a=e?.split("@")[0]?.trim();if(a){let e=a.replace(/[^a-zA-Z0-9]+/g," ").trim().split(/\s+/).filter(Boolean);if(e.length>=2)return`${e[0].charAt(0)}${e[1].charAt(0)}`.toUpperCase();if(1===e.length){let t=e[0];return t.length>=2?t.slice(0,2).toUpperCase():`${t.charAt(0)}`.toUpperCase()}}return t&&t.length>=2?t.slice(0,2).toUpperCase():t&&1===t.length?`${t.toUpperCase()}•`:"?"}(w,y),A=function(e){let t=0;for(let a=0;a<e.length;a+=1)t=e.charCodeAt(a)+((t<<5)-t);return Math.abs(t)%360}(S),z=(0,s.navAccountDisplayName)(w,y);return(0,t.jsxs)(g.Popover,{open:$,onOpenChange:C,children:["sidebar"===_?(0,t.jsxs)(g.PopoverTrigger,{render:(0,t.jsx)("button",{type:"button",className:(0,f.cn)("flex w-full items-center rounded-lg border border-transparent transition-colors hover:bg-sidebar-accent",j?"justify-center px-0 py-1":"gap-2.5 px-2 py-1.5 text-left"),"aria-label":`Account menu — ${N??"Unknown role"} — signed in as ${w||y||"unknown"}`,"aria-haspopup":"dialog",title:j?z:void 0}),children:[(0,t.jsx)(u.Avatar,{className:"size-[30px] shadow-inner ring-1 ring-black/5","aria-hidden":!0,children:(0,t.jsx)(u.AvatarFallback,{className:"font-semibold text-white",style:{backgroundColor:`hsl(${A} 46% 38%)`},children:I})}),!j&&(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("span",{className:"min-w-0 flex-1 leading-tight",children:[(0,t.jsx)("span",{className:"block truncate text-[13px] font-medium text-sidebar-foreground",children:z}),N&&(0,t.jsx)("span",{className:"block truncate text-[11px] text-muted-foreground",children:N})]}),(0,t.jsx)(n.ChevronsUpDown,{size:16,strokeWidth:1.75,className:"shrink-0 text-muted-foreground","aria-hidden":!0})]})]}):(0,t.jsxs)(g.PopoverTrigger,{render:(0,t.jsx)("button",{type:"button",className:"flex! max-w-[min(200px,34vw)] items-center gap-2 rounded-md! py-0.5! pl-1! pr-2! transition-colors hover:bg-accent!","aria-label":`Account menu — ${N??"Unknown role"} — signed in as ${w||y||"unknown"}`,"aria-haspopup":"dialog"}),children:[(0,t.jsx)(u.Avatar,{className:"shadow-inner ring-1 ring-black/5","aria-hidden":!0,children:(0,t.jsx)(u.AvatarFallback,{className:"font-semibold text-white",style:{backgroundColor:`hsl(${A} 46% 38%)`},children:I})}),(0,t.jsx)("span",{className:"hidden min-w-0 truncate text-left text-sm font-medium leading-none text-foreground md:inline",children:z}),(0,t.jsx)(i.ChevronDown,{className:"hidden size-2.5 shrink-0 text-muted-foreground md:inline","aria-hidden":!0})]}),(0,t.jsxs)(g.PopoverContent,{align:"sidebar"===_?"start":"end",side:"sidebar"===_?"top":"bottom",className:"w-auto gap-0 rounded-lg bg-card p-1 shadow-lg","data-testid":"user-dropdown-panel",children:[(0,t.jsxs)("div",{className:"flex w-full flex-col gap-2 p-3 text-sm",children:[(0,t.jsxs)("div",{className:"flex w-full items-center gap-2",children:[(0,t.jsx)(d.Mail,{className:"size-4"}),(0,t.jsx)("span",{className:"text-muted-foreground",children:w||"-"})]}),(0,t.jsx)(x.Separator,{className:"my-2"}),(0,t.jsxs)("div",{className:"flex w-full items-center justify-between gap-2",children:[(0,t.jsxs)("div",{className:"flex items-center gap-2",children:[(0,t.jsx)(p.User,{className:"size-4"}),(0,t.jsx)("span",{className:"text-muted-foreground",children:"User ID"})]}),(0,t.jsxs)("div",{className:"flex items-center gap-1",children:[(0,t.jsx)("span",{className:"max-w-[150px] truncate",title:y||"-",children:y||"-"}),(0,t.jsx)(h.default,{value:y,label:"Copy User ID"})]})]}),(0,t.jsxs)("div",{className:"flex w-full items-center justify-between gap-2",children:[(0,t.jsxs)("div",{className:"flex items-center gap-2",children:[(0,t.jsx)(m.ShieldCheck,{className:"size-4"}),(0,t.jsx)("span",{className:"text-muted-foreground",children:"Role"})]}),(0,t.jsx)("span",{children:N})]})]}),(0,t.jsx)(x.Separator,{}),"username_password"===k&&(0,t.jsxs)("button",{type:"button",onClick:()=>{C(!1),v.push((0,r.uiHref)("change-password"))},className:"flex w-full items-center gap-2 rounded-sm px-2 py-1.5 text-sm hover:bg-accent",children:[(0,t.jsx)(l.KeyRound,{className:"size-4"}),"Change Password"]}),(0,t.jsxs)("button",{type:"button",onClick:e,className:"flex w-full items-center gap-2 rounded-sm px-2 py-1.5 text-sm hover:bg-accent",children:[(0,t.jsx)(o.LogOut,{className:"size-4"}),"Logout"]})]})]})}])},853295,658140,e=>{"use strict";var t=e.i(843476),a=e.i(618566),s=e.i(755146),r=e.i(643531),i=e.i(344523),n=e.i(373264),l=e.i(271645),o=e.i(431703),d=e.i(602869);let m=(0,l.createContext)({mode:"ai-gateway",setMode:()=>{},plugins:[],activePlugin:null}),p="litellm_plugin_mode",c=(0,o.createApiClient)({getBaseUrl:()=>(0,d.getProxyBaseUrl)()??""});function u(){return localStorage.getItem(p)??"ai-gateway"}function g(){return(0,l.useContext)(m)}e.s(["PluginModeProvider",0,function({children:e,accessToken:a}){let[s,r]=(0,l.useState)(u),[i,n]=(0,l.useState)([]),[o,d]=(0,l.useState)(!1);(0,l.useEffect)(()=>{if(!a)return;let e=!1;return c.get("/api/plugins",{accessToken:a}).then(t=>{e||n(Array.isArray(t)?t:[])}).catch(()=>{}).finally(()=>{e||d(!0)}),()=>{e=!0}},[a]);let g="ai-gateway"!==s&&o&&!i.some(e=>e.name===s)?"ai-gateway":s,x=i.find(e=>e.name===g)??null;return(0,t.jsx)(m.Provider,{value:{mode:g,setMode:e=>{r(e),localStorage.setItem(p,e)},plugins:i,activePlugin:x},children:e})},"usePluginMode",0,g],658140);var x=e.i(292639),h=e.i(782066);let f="chat";e.s(["default",0,function(){let{mode:e,setMode:l,plugins:o}=g(),{data:d}=(0,x.useUISettings)(),m=(0,a.usePathname)(),p=!!d?.values?.enable_chat_ui,c=(0,h.uiHref)(f),u=(m??"").replace(/\/+$/,""),b=p&&(u===c||u.startsWith(`${c}/`)),_=b?"Chat":o.find(t=>t.name===e)?.display_name??"AI Gateway",j=[{key:"ai-gateway",label:"AI Gateway"},...o.map(e=>({key:e.name,label:e.display_name}))],y=p?{key:f,label:(0,t.jsxs)("div",{className:"flex items-center justify-between gap-6 py-0.5",children:[(0,t.jsx)("span",{className:"font-medium",children:"Chat"}),b&&(0,t.jsx)(r.Check,{className:"size-4 text-info"})]}),onClick:()=>window.location.assign((0,h.uiHref)(f))}:{key:f,disabled:!0,label:(0,t.jsxs)("div",{className:"flex max-w-[220px] flex-col py-0.5",children:[(0,t.jsx)("span",{className:"font-medium",children:"Chat"}),(0,t.jsx)("span",{className:"whitespace-normal text-xs leading-snug text-muted-foreground",children:"Admins can enable in Settings"})]})},w=[...j.map(a=>({key:a.key,label:(0,t.jsxs)("div",{className:"flex items-center justify-between gap-6 py-0.5",children:[(0,t.jsx)("span",{className:"font-medium",children:a.label}),!b&&a.key===e&&(0,t.jsx)(r.Check,{className:"size-4 text-info"})]}),onClick:()=>{l(a.key),b&&window.location.assign((0,h.uiHref)(""))}})),y];return(0,t.jsxs)(s.DropdownMenu,{children:[(0,t.jsxs)(s.DropdownMenuTrigger,{render:(0,t.jsx)("button",{type:"button",className:"flex h-8 max-w-[220px] items-center gap-1.5 rounded-md border border-border bg-background pl-1.5 pr-2 text-sm font-medium text-foreground transition-colors hover:bg-accent"}),children:[(0,t.jsx)("span",{className:"flex size-5 flex-none items-center justify-center rounded bg-muted text-muted-foreground",children:(0,t.jsx)(n.LayoutGrid,{className:"size-[13px]"})}),(0,t.jsx)("span",{className:"truncate",children:_}),(0,t.jsx)(i.ChevronsUpDown,{className:"size-3.5 flex-none text-muted-foreground"})]}),(0,t.jsx)(s.DropdownMenuContent,{className:"w-auto",children:w.map(e=>(0,t.jsx)(s.DropdownMenuItem,{disabled:e.disabled,onClick:e.onClick,children:e.label},e.key))})]})}],853295)},383862,e=>{"use strict";var t=e.i(843476),a=e.i(618393),s=e.i(131792),r=e.i(950594),i=e.i(283713);e.s(["default",0,({onWorkerSwitch:e})=>{let{isControlPlane:n,selectedWorker:l,workers:o}=(0,i.useWorker)();if(!n||!l)return null;let d=o.map(e=>({label:e.name,value:e.worker_id,disabled:e.worker_id===l.worker_id}));return(0,t.jsxs)(s.Combobox,{items:d,value:d.find(e=>e.value===l.worker_id)??null,itemToStringLabel:e=>e.label,onValueChange:t=>{t&&e(t.value)},children:[(0,t.jsx)(s.ComboboxInput,{className:"min-w-[180px]","aria-label":"Worker",children:(0,t.jsx)(r.InputGroupAddon,{align:"inline-start",children:(0,t.jsx)(a.Server,{className:"size-4"})})}),(0,t.jsxs)(s.ComboboxContent,{children:[(0,t.jsx)(s.ComboboxEmpty,{children:"No matching workers"}),(0,t.jsx)(s.ComboboxList,{children:e=>(0,t.jsx)(s.ComboboxItem,{value:e,disabled:e.disabled,children:e.label},e.value)})]})]})}])},455880,e=>{"use strict";var t=e.i(843476),a=e.i(475254);let s=(0,a.default)("moon",[["path",{d:"M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z",key:"a7tn18"}]]),r=(0,a.default)("sun",[["circle",{cx:"12",cy:"12",r:"4",key:"4exip2"}],["path",{d:"M12 2v2",key:"tus03m"}],["path",{d:"M12 20v2",key:"1lh1kg"}],["path",{d:"m4.93 4.93 1.41 1.41",key:"149t6j"}],["path",{d:"m17.66 17.66 1.41 1.41",key:"ptbguv"}],["path",{d:"M2 12h2",key:"1t8f8n"}],["path",{d:"M20 12h2",key:"1q8mjw"}],["path",{d:"m6.34 17.66-1.41 1.41",key:"1m8zz5"}],["path",{d:"m19.07 4.93-1.41 1.41",key:"1shlcs"}]]);var i=e.i(363178),n=e.i(519455);e.s(["default",0,()=>{let{setTheme:e,resolvedTheme:a}=(0,i.useTheme)(),l="dark"===a,o=l?"Switch to light mode":"Switch to dark mode";return(0,t.jsx)(n.Button,{variant:"ghost",size:"icon-sm","aria-label":o,title:o,className:"text-muted-foreground",onClick:()=>e(l?"light":"dark"),children:l?(0,t.jsx)(s,{}):(0,t.jsx)(r,{})})}],455880)},909947,e=>{"use strict";var t=e.i(865361);e.s(["generateCodeSnippet",0,e=>{let a,{apiKeySource:s,accessToken:r,apiKey:i,inputMessage:n,chatHistory:l,selectedTags:o,selectedVectorStores:d,selectedGuardrails:m,selectedPolicies:p,selectedVoice:c,endpointType:u,selectedModel:g,selectedSdk:x,proxySettings:h,customHeaders:f}=e,b="session"===s?r:i,_=window.location.origin,j=h?.LITELLM_UI_API_DOC_BASE_URL;j&&j.trim()?_=j:h?.PROXY_BASE_URL&&(_=h.PROXY_BASE_URL);let y=n||"Your prompt here",w=y.replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n"),N=l.filter(e=>!e.isImage).map(({role:e,content:t})=>({role:e,content:t})),k={};o.length>0&&(k.tags=o),d.length>0&&(k.vector_stores=d),m.length>0&&(k.guardrails=m),p.length>0&&(k.policies=p);let v=g||"your-model-name",$=f&&Object.keys(f).length>0?`,
	default_headers=${JSON.stringify(f,null,2).replace(/\n/g,"\n	")}`:"",C="azure"===x?`import openai

client = openai.AzureOpenAI(
	api_key="${b||"YOUR_LITELLM_API_KEY"}",
	azure_endpoint="${_}",
	api_version="2024-02-01"${$}
)`:`import openai

client = openai.OpenAI(
	api_key="${b||"YOUR_LITELLM_API_KEY"}",
	base_url="${_}"${$}
)`;switch(u){case t.EndpointType.CHAT:{let e=Object.keys(k).length>0,t="";if(e){let e=JSON.stringify({metadata:k},null,2).split("\n").map(e=>" ".repeat(4)+e).join("\n").trim();t=`,
    extra_body=${e}`}let s=N.length>0?N:[{role:"user",content:y}];a=`
import base64

# Helper function to encode images to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Example with text only
response = client.chat.completions.create(
    model="${v}",
    messages=${JSON.stringify(s,null,4)}${t}
)

print(response)

# Example with image or PDF (uncomment and provide file path to use)
# base64_file = encode_image("path/to/your/file.jpg")  # or .pdf
# response_with_file = client.chat.completions.create(
#     model="${v}",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "${w}"
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
    extra_body=${e}`}let s=N.length>0?N:[{role:"user",content:y}];a=`
import base64

# Helper function to encode images to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Example with text only
response = client.responses.create(
    model="${v}",
    input=${JSON.stringify(s,null,4)}${t}
)

print(response.output_text)

# Example with image or PDF (uncomment and provide file path to use)
# base64_file = encode_image("path/to/your/file.jpg")  # or .pdf
# response_with_file = client.responses.create(
#     model="${v}",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "input_text", "text": "${w}"},
#                 {
#                     "type": "input_image",
#                     "image_url": f"data:image/jpeg;base64,{base64_file}",  # or data:application/pdf;base64,{base64_file}
#                 },
#             ],
#         }
#     ]${t}
# )
# print(response_with_file.output_text)
`;break}case t.EndpointType.IMAGE:a="azure"===x?`
# NOTE: The Azure SDK does not have a direct equivalent to the multi-modal 'responses.create' method shown for OpenAI.
# This snippet uses 'client.images.generate' and will create a new image based on your prompt.
# It does not use the uploaded image, as 'client.images.generate' does not support image inputs in this context.
import os
import requests
import json
import time
from PIL import Image

result = client.images.generate(
	model="${v}",
	prompt="${n}",
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
prompt = "${w}"

# Encode images to base64
base64_image1 = encode_image("body-lotion.png")
base64_image2 = encode_image("soap.png")

# Create file IDs
file_id1 = create_file("body-lotion.png")
file_id2 = create_file("incense-kit.png")

response = client.responses.create(
	model="${v}",
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
`;break;case t.EndpointType.IMAGE_EDITS:a="azure"===x?`
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
prompt = "${w}"

# Encode images to base64
base64_image1 = encode_image("body-lotion.png")
base64_image2 = encode_image("soap.png")

# Create file IDs
file_id1 = create_file("body-lotion.png")
file_id2 = create_file("incense-kit.png")

response = client.responses.create(
	model="${v}",
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
prompt = "${w}"

# Encode images to base64
base64_image1 = encode_image("body-lotion.png")
base64_image2 = encode_image("soap.png")

# Create file IDs
file_id1 = create_file("body-lotion.png")
file_id2 = create_file("incense-kit.png")

response = client.responses.create(
	model="${v}",
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
`;break;case t.EndpointType.EMBEDDINGS:a=`
response = client.embeddings.create(
	input="${n||"Your string here"}",
	model="${v}",
	encoding_format="base64" # or "float"
)

print(response.data[0].embedding)
`;break;case t.EndpointType.TRANSCRIPTION:a=`
# Open the audio file
audio_file = open("path/to/your/audio/file.mp3", "rb")

# Make the transcription request
response = client.audio.transcriptions.create(
	model="${v}",
	file=audio_file${n?`,
	prompt="${n.replace(/\\/g,"\\\\").replace(/"/g,'\\"')}"`:""}
)

print(response.text)
`;break;case t.EndpointType.SPEECH:a=`
# Make the text-to-speech request
response = client.audio.speech.create(
	model="${v}",
	input="${n||"Your text to convert to speech here"}",
	voice="${c}"  # Options: alloy, ash, ballad, coral, echo, fable, nova, onyx, sage, shimmer
)

# Save the audio to a file
output_filename = "output_speech.mp3"
response.stream_to_file(output_filename)
print(f"Audio saved to {output_filename}")

# Optional: Customize response format and speed
# response = client.audio.speech.create(
#     model="${v}",
#     input="${n||"Your text to convert to speech here"}",
#     voice="alloy",
#     response_format="mp3",  # Options: mp3, opus, aac, flac, wav, pcm
#     speed=1.0  # Range: 0.25 to 4.0
# )
# response.stream_to_file("output_speech.mp3")
`;break;default:a="\n# Code generation for this endpoint is not implemented yet."}return`${C}
${a}`}])},652272,209261,e=>{"use strict";var t=e.i(843476),a=e.i(271645),s=e.i(871689),r=e.i(643531),i=e.i(174886),n=e.i(306228),l=e.i(196631);let o=/^[a-zA-Z0-9][a-zA-Z0-9._-]*(\/[a-zA-Z0-9][a-zA-Z0-9._-]*)*$/,d=e=>e.trim().replace(/\/+$/,""),m=/\.(md|markdown|txt|json|ya?ml|toml)$/i,p=/\.zip$/i,c=/^[0-9a-fA-F]{64}$/,u=/^\d{1,3}(\.\d{1,3}){3}$/,g=/^[A-Za-z0-9-]+$/,x=/^[A-Za-z0-9._-]+$/,h=/^https?:\/\//i,f="ssh://",b=/^([a-z0-9._-]+)@([^:/@]+):(?!\/)(.+)$/i,_=e=>e.pathname.split("/").filter(e=>""!==e),j=e=>{try{return new URL(e)}catch{return null}},y=e=>e.hostname.includes(".")&&!e.hostname.startsWith("[")&&!u.test(e.hostname),w=e=>{let t=e.split("/").filter(e=>""!==e);return t[t.length-1]??""},N=e=>e.toLowerCase().replace(/[^a-z0-9-]+/g,"-").replace(/-+/g,"-").replace(/^-+|-+$/g,""),k=(e,t,a,s)=>{let r=d(s??"");return""!==r?o.test(r)?{parsed:{source:"git-subdir",url:t,path:r},label:`${e} subdir — ${t} @ ${r}`,suggestedName:N(w(r))}:null:{parsed:{source:"url",url:t},label:`${e} repo — ${t}`,suggestedName:N(a)}},v=e=>JSON.stringify({extraKnownMarketplaces:{litellm:{source:{source:"url",url:`${e}/claude-code/marketplace.json`}}}},null,2),$=e=>`/plugin install ${e.name}@litellm`,C=e=>"github"===e.source&&e.repo?`GitHub: ${e.repo}`:"git-subdir"===e.source&&e.url&&e.path?`${e.url} @ ${e.path}`:("url"===e.source||"archive"===e.source)&&e.url?e.url:"Unknown source",S=e=>"github"===e.source&&e.repo?`https://github.com/${e.repo}`:("url"===e.source||"git-subdir"===e.source||"archive"===e.source)&&e.url&&h.test(e.url)?e.url:null;e.s(["buildMarketplaceSettingsSnippet",0,v,"formatInstallCommand",0,$,"getCategoryBadgeColor",0,e=>{if(!e)return"gray";let t=e.toLowerCase();if(t.includes("development")||t.includes("dev"))return"blue";if(t.includes("productivity")||t.includes("workflow"))return"green";if(t.includes("learning")||t.includes("education"))return"purple";if(t.includes("security")||t.includes("safety"))return"red";if(t.includes("data")||t.includes("analytics"))return"orange";else if(t.includes("integration")||t.includes("api"))return"yellow";return"gray"},"getSourceDisplayText",0,C,"getSourceLink",0,S,"isValidEmail",0,e=>!e||/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e),"isValidSemanticVersion",0,e=>!e||/^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?(\+[a-zA-Z0-9.-]+)?$/.test(e),"isValidSha256",0,e=>""===e.trim()||c.test(e.trim()),"isValidSubPath",0,e=>{let t=d(e);return""!==t&&o.test(t)},"parseKeywords",0,e=>e&&""!==e.trim()?e.split(",").map(e=>e.trim()).filter(e=>""!==e):[],"parseSkillSource",0,(e,t)=>{let a=((e,t)=>{let a=e.trim(),s=b.exec(a),r=s?`${f}${s[1]}@${s[2]}/${s[3]}`:a;if(!r.toLowerCase().startsWith(f))return null;let i=j(r);if(!i||""===i.username||""!==i.password||!y(i))return null;let n=r.indexOf("/",f.length);return -1===n||i.pathname!==r.slice(n)||_(i).length<2?null:k("SSH",a,w(i.pathname).replace(/\.git$/i,""),t)})(e,t);if(a)return a;let s=(e=>{let t=e.trim();if(""===t||t.startsWith("//"))return null;let a=j(/^[a-z][a-z0-9+.-]*:\/\//i.test(t)?t:`https://${t}`);return a&&"https:"===a.protocol&&""===a.username&&""===a.password&&y(a)?a:null})(e);if(!s)return null;if(p.test(s.pathname))return{parsed:{source:"archive",url:s.href},label:`Zip archive — ${s.host}${s.pathname}`,suggestedName:N(w(s.pathname).replace(p,""))};if("github.com"===s.hostname.replace(/^www\./,""))return((e,t)=>{let a=_(e);if(a.length<2)return null;let s=a[0],r=a[1].replace(/\.git$/,"");if(!g.test(s)||!x.test(r))return null;let i=`${s}/${r}`,n=`https://github.com/${i}`,l={parsed:{source:"github",repo:i},label:`GitHub repo — ${i}`,suggestedName:N(r)};if(a.length>=4&&("tree"===a[2]||"blob"===a[2])){let e=a.slice(4),t=w(e.join("/")),s=m.test(t)?e.slice(0,-1):e;if(0===s.length)return l;let r=d(s.join("/"));return o.test(r)?{parsed:{source:"git-subdir",url:n,path:r},label:`GitHub subdir — ${i} @ ${r}`,suggestedName:N(w(r))}:null}if(2!==a.length)return null;let p=d(t??"");return""!==p?o.test(p)?{parsed:{source:"git-subdir",url:n,path:p},label:`GitHub subdir — ${i} @ ${p}`,suggestedName:N(w(p))}:null:l})(s,t);if(_(s).length<2)return null;let r=w(s.pathname).replace(/\.git$/,"");return k("Git",`${s.protocol}//${s.host}${s.pathname.replace(/\/+$/,"")}`,r,t)},"validatePluginName",0,e=>!!e&&""!==e.trim()&&/^[a-z0-9-]+$/.test(e)],209261);let I=({source:e})=>{let a=S(e),s=a&&"git-subdir"===e.source&&e.path?`${a}/tree/main/${e.path}`:a;return s?(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Source"}),(0,t.jsxs)("a",{href:s,target:"_blank",rel:"noopener noreferrer",className:"flex items-center gap-1 break-all text-[13px] text-info",children:[s.replace("https://",""),(0,t.jsx)(n.Link2,{className:"size-3 shrink-0"})]})]}):e.url?(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Source"}),(0,t.jsx)("div",{className:"break-all text-[13px] text-foreground",children:C(e)})]}):null};e.s(["default",0,({skill:e,onBack:n})=>{let[o,d]=(0,a.useState)("overview"),[m,p]=(0,a.useState)(null),c=(e,t)=>{navigator.clipboard.writeText(e),p(t),setTimeout(()=>p(null),2e3)},u=$(e),g=v(window.location.origin),x=[...e.category?[{property:"Category",value:e.category}]:[],...e.domain?[{property:"Domain",value:e.domain}]:[],...e.namespace?[{property:"Namespace",value:e.namespace}]:[],...e.version?[{property:"Version",value:e.version}]:[],...e.author?.name?[{property:"Author",value:e.author.name}]:[],...e.created_at?[{property:"Added",value:new Date(e.created_at).toLocaleDateString()}]:[]];return(0,t.jsxs)("div",{className:"py-6 pl-0 pr-8",children:[(0,t.jsxs)("div",{onClick:n,className:"mb-6 inline-flex cursor-pointer items-center gap-1.5 text-sm text-muted-foreground",children:[(0,t.jsx)(s.ArrowLeft,{className:"size-3"}),(0,t.jsx)("span",{children:"Skills"})]}),(0,t.jsxs)("div",{className:"mb-2",children:[(0,t.jsx)("h1",{className:"m-0 text-[28px] font-normal leading-tight text-foreground",children:e.name}),e.description&&(0,t.jsx)("p",{className:"mb-0 ml-0 mr-0 mt-2 text-sm leading-relaxed text-muted-foreground",children:e.description})]}),(0,t.jsx)("div",{className:"mb-7 mt-6 border-b border-border",children:(0,t.jsx)("div",{className:"flex",children:[{key:"overview",label:"Overview"},{key:"usage",label:"How to Use"}].map(e=>(0,t.jsx)("div",{onClick:()=>d(e.key),className:(0,l.cn)("-mb-px cursor-pointer border-b-[3px] px-5 py-3 text-sm",o===e.key?"border-info font-medium text-info":"border-transparent font-normal text-muted-foreground"),children:e.label},e.key))})}),"overview"===o&&(0,t.jsxs)("div",{className:"flex gap-16",children:[(0,t.jsxs)("div",{className:"min-w-0 flex-1",children:[(0,t.jsx)("h2",{className:"m-0 mb-1 text-lg font-normal text-foreground",children:"Skill Details"}),(0,t.jsx)("p",{className:"m-0 mb-4 text-[13px] text-muted-foreground",children:"Metadata registered with this skill"}),(0,t.jsxs)("table",{className:"w-full border-collapse text-sm",children:[(0,t.jsx)("thead",{children:(0,t.jsxs)("tr",{className:"border-b border-border",children:[(0,t.jsx)("th",{className:"w-40 py-3 text-left font-medium text-muted-foreground",children:"Property"}),(0,t.jsx)("th",{className:"py-3 text-left font-medium text-muted-foreground",children:e.name})]})}),(0,t.jsx)("tbody",{children:x.map((e,a)=>(0,t.jsxs)("tr",{className:"border-b border-border",children:[(0,t.jsx)("td",{className:"py-3 text-foreground",children:e.property}),(0,t.jsx)("td",{className:"py-3 text-foreground",children:e.value})]},a))})]})]}),(0,t.jsxs)("div",{className:"w-60 shrink-0",children:[(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Status"}),(0,t.jsx)("span",{className:(0,l.cn)("rounded-xl px-2.5 py-[3px] text-xs font-medium",e.enabled?"bg-success/10 text-success":"bg-muted text-muted-foreground"),children:e.enabled?"Public":"Draft"})]}),(0,t.jsx)(I,{source:e.source}),e.keywords&&e.keywords.length>0&&(0,t.jsxs)("div",{className:"mb-6",children:[(0,t.jsx)("div",{className:"mb-2 text-xs text-muted-foreground",children:"Tags"}),(0,t.jsx)("div",{className:"flex flex-wrap gap-1.5",children:e.keywords.map(e=>(0,t.jsx)("span",{className:"rounded-2xl border border-border bg-card px-3 py-1 text-xs text-foreground",children:e},e))})]}),(0,t.jsxs)("div",{children:[(0,t.jsx)("div",{className:"mb-1 text-xs text-muted-foreground",children:"Skill ID"}),(0,t.jsx)("div",{className:"break-all font-mono text-xs text-foreground",children:e.id})]})]})]}),"usage"===o&&(0,t.jsxs)("div",{className:"max-w-[640px]",children:[(0,t.jsx)("h2",{className:"m-0 mb-2 text-lg font-normal text-foreground",children:"Using this skill"}),(0,t.jsx)("p",{className:"m-0 mb-6 text-sm leading-relaxed text-muted-foreground",children:"Once your proxy is set as a marketplace, enable this skill in Claude Code with one command:"}),(0,t.jsxs)("div",{className:"mb-6 overflow-hidden rounded-lg border border-border",children:[(0,t.jsxs)("div",{className:"flex items-center justify-between border-b border-border bg-muted px-4 py-2.5",children:[(0,t.jsx)("span",{className:"text-[13px] font-medium text-foreground",children:"Run in Claude Code"}),(0,t.jsxs)("button",{onClick:()=>c(u,"install"),className:(0,l.cn)("flex cursor-pointer items-center gap-1 border-none bg-transparent p-0 text-xs","install"===m?"text-success":"text-info"),children:["install"===m?(0,t.jsx)(r.Check,{className:"size-3"}):(0,t.jsx)(i.Copy,{className:"size-3"}),"install"===m?"Copied":"Copy"]})]}),(0,t.jsx)("pre",{className:"m-0 bg-card px-4 py-3.5 font-mono text-sm text-foreground",children:u})]}),(0,t.jsxs)("div",{className:"mb-4 rounded-lg border border-warning/30 bg-warning/10 px-4 py-3",children:[(0,t.jsxs)("p",{className:"m-0 mb-2 text-[13px] leading-relaxed text-muted-foreground",children:['If you see "Plugin ',e.name,' not found in marketplace", update the catalog first:']}),(0,t.jsx)("pre",{className:"m-0 bg-transparent font-mono text-[13px] text-foreground",children:"/plugin marketplace update litellm"})]}),(0,t.jsxs)("p",{className:"m-0 text-[13px] leading-relaxed text-muted-foreground",children:["Don't have the marketplace configured yet?"," ",(0,t.jsx)("span",{onClick:()=>d("setup"),className:"cursor-pointer text-info",children:"See one-time setup →"})]})]}),"setup"===o&&(0,t.jsxs)("div",{className:"max-w-[640px]",children:[(0,t.jsx)("h2",{className:"m-0 mb-2 text-lg font-normal text-foreground",children:"One-time marketplace setup"}),(0,t.jsx)("p",{className:"m-0 mb-3 text-sm leading-relaxed text-muted-foreground",children:"Run this command in Claude Code to register the marketplace:"}),(0,t.jsxs)("div",{className:"mb-6 overflow-hidden rounded-lg border border-border",children:[(0,t.jsxs)("div",{className:"flex items-center justify-between border-b border-border bg-muted px-4 py-2.5",children:[(0,t.jsx)("span",{className:"text-[13px] font-medium text-foreground",children:"Run in Claude Code"}),(0,t.jsxs)("button",{onClick:()=>{let e=window.location.origin;c(`/plugin marketplace add ${e}/claude-code/marketplace.json`,"marketplace-cmd")},className:(0,l.cn)("flex cursor-pointer items-center gap-1 border-none bg-transparent p-0 text-xs","marketplace-cmd"===m?"text-success":"text-info"),children:["marketplace-cmd"===m?(0,t.jsx)(r.Check,{className:"size-3"}):(0,t.jsx)(i.Copy,{className:"size-3"}),"marketplace-cmd"===m?"Copied":"Copy"]})]}),(0,t.jsx)("pre",{className:"m-0 bg-card px-4 py-3.5 font-mono text-[13px] text-foreground",children:`/plugin marketplace add ${window.location.origin}/claude-code/marketplace.json`})]}),(0,t.jsxs)("p",{className:"m-0 mb-3 text-sm leading-relaxed text-muted-foreground",children:["Or add this to ",(0,t.jsx)("code",{className:"rounded bg-muted px-1.5 py-px text-[13px]",children:"~/.claude/settings.json"})," ","for a persistent configuration:"]}),(0,t.jsxs)("div",{className:"overflow-hidden rounded-lg border border-border",children:[(0,t.jsxs)("div",{className:"flex items-center justify-between border-b border-border bg-muted px-4 py-2.5",children:[(0,t.jsx)("span",{className:"text-[13px] font-medium text-foreground",children:"~/.claude/settings.json"}),(0,t.jsxs)("button",{onClick:()=>c(g,"settings"),className:(0,l.cn)("flex cursor-pointer items-center gap-1 border-none bg-transparent p-0 text-xs","settings"===m?"text-success":"text-info"),children:["settings"===m?(0,t.jsx)(r.Check,{className:"size-3"}):(0,t.jsx)(i.Copy,{className:"size-3"}),"settings"===m?"Copied":"Copy"]})]}),(0,t.jsx)("pre",{className:"m-0 bg-card px-4 py-3.5 font-mono text-[13px] text-foreground",children:g})]})]})]})}],652272)},402874,e=>{"use strict";var t=e.i(843476),a=e.i(283713),s=e.i(602869),r=e.i(782066),i=e.i(275144),n=e.i(886400),l=e.i(321836),o=e.i(972518),d=e.i(799647),m=e.i(522016),p=e.i(196631),c=e.i(641141),u=e.i(455880),g=e.i(853295),x=e.i(383862);let h="h-auto max-h-full w-auto max-w-full object-contain";e.s(["default",0,({accessToken:e,isPublicPage:f=!1,sidebarCollapsed:b=!1,onToggleSidebar:_})=>{let j=(0,s.getProxyBaseUrl)(),{logoUrl:y}=(0,i.useTheme)(),{isControlPlane:w,selectedWorker:N}=(0,a.useWorker)(),k=y||`${j}/get_image`,v=y||`${j}/get_image?theme=dark`,$=(0,n.useLogout)(e);return(0,t.jsx)("nav",{className:"sticky top-0 z-chrome border-b border-border bg-card",children:(0,t.jsx)("div",{className:"w-full",children:(0,t.jsxs)("div",{className:"flex h-14 items-center px-4",children:[(0,t.jsxs)("div",{className:"flex shrink-0 items-center",children:[_&&(0,t.jsx)("button",{onClick:_,className:"mr-2 flex h-9 w-9 items-center justify-center rounded-md text-muted-foreground transition-colors hover:bg-accent hover:text-foreground",title:b?"Expand sidebar":"Collapse sidebar",children:(0,t.jsx)("span",{className:"text-lg",children:b?(0,t.jsx)(d.PanelLeftOpen,{className:"size-[18px]"}):(0,t.jsx)(o.PanelLeftClose,{className:"size-[18px]"})})}),(0,t.jsx)("div",{className:"flex items-center gap-2",children:(0,t.jsx)(m.default,{href:(0,r.uiHref)(""),className:"flex items-center",children:(0,t.jsx)("div",{className:"relative",children:(0,t.jsxs)("div",{className:"flex h-10 max-w-48 items-center justify-center overflow-hidden",children:[(0,t.jsx)("img",{src:k,alt:"EmbRouter Brand",className:(0,p.cn)(h,"dark:hidden")}),(0,t.jsx)("img",{src:v,alt:"","aria-hidden":!0,className:(0,p.cn)(h,"hidden dark:block")})]})})})})]}),!f&&(0,t.jsx)("div",{className:"ml-4 flex shrink-0 items-center border-l border-border pl-4",children:(0,t.jsx)(g.default,{})}),(0,t.jsxs)("div",{className:"ml-auto flex min-w-0 flex-1 items-center justify-end gap-4",children:[w&&null!==N&&(0,t.jsx)("div",{className:"flex shrink-0 items-center",children:(0,t.jsx)(x.default,{onWorkerSwitch:t=>{(0,n.revokeSessionAndClearClientState)(e).finally(()=>{window.location.href=`${(0,l.getLoginUrl)()}?worker=${encodeURIComponent(t)}`})}})}),!f&&(0,t.jsx)("div",{className:"flex shrink-0 items-center border-l border-border pl-4",children:(0,t.jsxs)("div",{className:"flex items-center gap-0.5 rounded-lg bg-muted px-1 py-0 transition-colors hover:bg-accent",children:[(0,t.jsx)(u.default,{}),(0,t.jsx)("span",{className:"mx-0.5 h-6 w-px shrink-0 bg-border","aria-hidden":!0}),(0,t.jsx)(c.default,{onLogout:$})]})})]})]})})})}])},283713,e=>{"use strict";var t=e.i(271645),a=e.i(602869),s=e.i(612256);let r="litellm_selected_worker_id";e.s(["useWorker",0,()=>{let{data:e}=(0,s.useUIConfig)(),i=e?.is_control_plane??!1,n=e?.workers??[],[l,o]=(0,t.useState)(()=>localStorage.getItem(r));(0,t.useEffect)(()=>{if(!l||0===n.length)return;let e=n.find(e=>e.worker_id===l);e&&(0,a.switchToWorkerUrl)(e.url)},[l,n]);let d=n.find(e=>e.worker_id===l)??null,m=(0,t.useCallback)(e=>{let t=n.find(t=>t.worker_id===e);t&&(o(e),localStorage.setItem(r,e),(0,a.switchToWorkerUrl)(t.url))},[n]);return{isControlPlane:i,workers:n,selectedWorkerId:l,selectedWorker:d,selectWorker:m,disconnectFromWorker:(0,t.useCallback)(()=>{o(null),localStorage.removeItem(r),(0,a.switchToWorkerUrl)(null)},[])}}])},899426,e=>{"use strict";let t=e=>e.trim().toLowerCase();function a(e,a){let s=t(e);if(""===s)return!0;let r=a.filter(e=>"string"==typeof e).map(e=>e.toLowerCase());return!!r.some(e=>e.includes(s))||s.split(/\s+/).every(e=>r.some(t=>t.includes(e)))}e.s(["filterBySearchTerm",0,function(e,t,s){return e.filter(e=>a(t,s(e)))},"matchesSearchTerm",0,a,"rankBySearchRelevance",0,function(e,a,s){let r=t(a);if(""===r)return[...e];let i=e=>{let t=s(e).toLowerCase();return 1e3*(t===r)+100*!!t.startsWith(r)+(1e3-t.length)};return[...e].sort((e,t)=>i(t)-i(e))}])}]);