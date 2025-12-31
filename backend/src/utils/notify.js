let sgMail = null;
let twilio = null;
try {
  sgMail = require('@sendgrid/mail');
} catch (e) {
  sgMail = null;
}
try {
  twilio = require('twilio');
} catch (e) {
  twilio = null;
}

const SENDGRID_API_KEY = process.env.SENDGRID_API_KEY;
const TWILIO_ACCOUNT_SID = process.env.TWILIO_ACCOUNT_SID;
const TWILIO_AUTH_TOKEN = process.env.TWILIO_AUTH_TOKEN;
const TWILIO_WHATSAPP_FROM = process.env.TWILIO_WHATSAPP_FROM; // e.g. 'whatsapp:+123456789'
const NOTIFY_EMAIL_TO = process.env.NOTIFY_EMAIL_TO; // email to receive alerts

if (sgMail && SENDGRID_API_KEY) sgMail.setApiKey(SENDGRID_API_KEY);

let twClient = null;
if (twilio && TWILIO_ACCOUNT_SID && TWILIO_AUTH_TOKEN) twClient = twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN);

async function sendEmail(subject, text, to = NOTIFY_EMAIL_TO) {
  if (!SENDGRID_API_KEY || !to) return Promise.resolve();
  const msg = {
    to,
    from: process.env.SENDGRID_FROM_EMAIL || to,
    subject,
    text,
  };
  return sgMail.send(msg);
}

async function sendWhatsApp(toNumber, text) {
  if (!twClient || !TWILIO_WHATSAPP_FROM) return Promise.resolve();
  return twClient.messages.create({ from: TWILIO_WHATSAPP_FROM, to: `whatsapp:${toNumber}`, body: text });
}

async function notifyGuestbook(entry) {
  const subject = `Guestbook: ${entry.name}`;
  const text = `New guestbook message from ${entry.name}\n\n${entry.message}\n\nEmail: ${entry.email || 'N/A'}`;
  await sendEmail(subject, text);
  // optional WhatsApp notify number from env
  const notifyPhone = process.env.NOTIFY_WHATSAPP_TO;
  if (notifyPhone) await sendWhatsApp(notifyPhone, text);
}

async function notifyContact(form) {
  const subject = `Contact: ${form.name || 'Visitor'}`;
  const text = `Message from ${form.name || 'Visitor'}\nEmail: ${form.email || 'N/A'}\n\n${form.message}`;
  await sendEmail(subject, text);
  const notifyPhone = process.env.NOTIFY_WHATSAPP_TO;
  if (notifyPhone) await sendWhatsApp(notifyPhone, text);
}

module.exports = { notifyGuestbook, notifyContact, sendEmail, sendWhatsApp };
