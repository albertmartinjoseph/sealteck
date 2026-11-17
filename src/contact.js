export function validateContact(values){
 const errors={};
 if(!values.fullName?.trim())errors.fullName='Enter your full name.';
 if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(values.email||''))errors.email='Enter a valid email address.';
 if(values.phone&&!/^[+\d\s().-]{7,25}$/.test(values.phone))errors.phone='Enter a valid phone number, or leave this field blank.';
 if(!values.subject?.trim())errors.subject='Enter a subject.';
 if(!values.message?.trim())errors.message='Enter your message.';
 return errors;
}
// Supply an endpoint adapter here when online submissions are enabled.
// Never treat a local UI action as successful message delivery.
export async function submitContact(values,adapter){
 if(!adapter)throw new Error('Online submissions are not yet available.');
 const errors=validateContact(values);
 if(Object.keys(errors).length)throw new Error('Please correct the highlighted fields.');
 return adapter(values);
}
