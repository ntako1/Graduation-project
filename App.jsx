/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React from 'react';
import { Amplify } from 'aws-amplify';
import awsExports from './src/aws-exports';
import Navigation from './src/navigation';
import NotificationManager from './src/components/CustomScreenComps/NotificationManager';

Amplify.configure(awsExports);

const App = () => {
  return (
    <>
      <NotificationManager />
      <Navigation />
    </>
  );
};

export default App;
