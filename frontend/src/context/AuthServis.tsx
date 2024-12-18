import apiClient from "../apiClient";

export interface LoginResult {
  success: boolean;
  token?: string;
  error?: string;
}

export interface RegisterResult {
  success: boolean;
  error?: string;
}

export class AuthService {
  private static API_BASE_URL = "/auth";

  static async login(username: string, password: string): Promise<LoginResult> {
    try {
      const response = await apiClient.post(`${this.API_BASE_URL}/token/login/`, {
        username,
        password,
      });

      return { success: true, token: response.data.auth_token };
    } catch (error: any) {
      const errorMessage =
        error.response?.data?.detail || "Ошибка при логине";
      return { success: false, error: errorMessage };
    }
  }

  static async register(
    username: string,
    password: string,
    email: string
  ): Promise<RegisterResult> {
    try {
      await apiClient.post(`${this.API_BASE_URL}/users/`, {
        username,
        password,
        email,
      });

      return { success: true };
    } catch (error: any) {
      const errorMessage =
        error.response?.data?.detail || "Ошибка при регистрации";
      return { success: false, error: errorMessage };
    }
  }
}