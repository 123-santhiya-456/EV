import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyAnb2wKWv5Mx0aY4yWumYrfB69AX1jK7hM",
  authDomain: "evconnect-60823.firebaseapp.com",
  projectId: "evconnect-60823",
  storageBucket: "evconnect-60823.firebasestorage.app",
  messagingSenderId: "862815489749",
  appId: "1:862815489749:web:2e47e3a1efc2f698c05c5c"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const googleProvider = new GoogleAuthProvider();

export { app, auth, db, googleProvider };