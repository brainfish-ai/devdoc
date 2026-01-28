/**
 * API Client
 * Auto-generated from OpenAPI specification
 */

import type { paths, components } from './types';

export type ApiPaths = paths;
export type ApiComponents = components;

export interface ClientConfig {
  baseUrl: string;
  headers?: Record<string, string>;
}

let config: ClientConfig = {
  baseUrl: '',
};

export function setConfig(newConfig: Partial<ClientConfig>) {
  config = { ...config, ...newConfig };
}

export function getConfig(): ClientConfig {
  return config;
}

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

export async function request<T = unknown>(
  method: HttpMethod,
  path: string,
  options?: {
    params?: Record<string, string | number | boolean>;
    body?: unknown;
    headers?: Record<string, string>;
  }
): Promise<T> {
  let url = `${config.baseUrl}${path}`;
  
  // Add query params
  if (options?.params) {
    const searchParams = new URLSearchParams();
    for (const [key, value] of Object.entries(options.params)) {
      searchParams.append(key, String(value));
    }
    url += `?${searchParams.toString()}`;
  }

  const response = await fetch(url, {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...config.headers,
      ...options?.headers,
    },
    body: options?.body ? JSON.stringify(options.body) : undefined,
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

export const client = {
  get: <T = unknown>(path: string, options?: { params?: Record<string, string | number | boolean>; headers?: Record<string, string> }) => 
    request<T>('GET', path, options),
  post: <T = unknown>(path: string, body?: unknown, options?: { headers?: Record<string, string> }) => 
    request<T>('POST', path, { body, ...options }),
  put: <T = unknown>(path: string, body?: unknown, options?: { headers?: Record<string, string> }) => 
    request<T>('PUT', path, { body, ...options }),
  patch: <T = unknown>(path: string, body?: unknown, options?: { headers?: Record<string, string> }) => 
    request<T>('PATCH', path, { body, ...options }),
  delete: <T = unknown>(path: string, options?: { headers?: Record<string, string> }) => 
    request<T>('DELETE', path, options),
};
