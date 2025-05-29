import React from 'react';
import Layout from '@theme-original/Layout';
import { CookieSeal } from '../../components/CookieSeal';

export default function CustomLayout(props) {
  return (
    <>
      <Layout {...props} />
      <CookieSeal />
    </>
  );
}