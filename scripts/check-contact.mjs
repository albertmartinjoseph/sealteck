import {chromium} from '@playwright/test';
import assert from 'node:assert/strict';
import {validateContact} from '../src/contact.js';
assert.equal(Object.keys(validateContact({})).length,4);
assert.deepEqual(validateContact({fullName:'Alex',email:'alex@example.com',subject:'Enquiry',message:'Hello',phone:'+44 7776 683424'}),{});
const b=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const p=await b.newPage({viewport:{width:375,height:850}});await p.goto('http://127.0.0.1:5173/contact-us');
for(const name of ['Full Name','Email Address','Phone Number','Company Name','Subject','Message'])await p.getByLabel(name,{exact:false}).waitFor();
assert(await p.getByRole('button',{name:'Send message'}).isDisabled());await p.getByLabel('Email Address').fill('invalid');await p.getByLabel('Message').focus();assert.equal(await p.getByLabel('Email Address').getAttribute('aria-invalid'),'true');await p.getByText('Enter a valid email address.',{exact:true}).waitFor();await p.getByLabel('Email Address').fill('alex@example.com');await p.getByLabel('Message').focus();assert.equal(await p.getByLabel('Email Address').getAttribute('aria-invalid'),'false');assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await b.close();console.log('Contact: six fields, disabled submission, accessible email validation and phone layout passed.');
