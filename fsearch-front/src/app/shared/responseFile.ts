import { Document } from "./doc"

export interface ResponseFile {
    "search_words"?: string,
    "docs": Document[]
}