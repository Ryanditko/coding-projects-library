(ns gerador-de-senha.main
  (:require [clojure.string :as str]))

(def letras-maiusculas "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
(def letras-minusculas "abcdefghijklmnopqrstuvwxyz")
(def numeros "0123456789")
(def simbolos "!@#$%^&*()-_=+[]{}|;:',.<>?/`~")

(defn gerar-senha [tamanho]
  (let [caracteres (str letras-maiusculas letras-minusculas numeros simbolos)
        caracteres-list (vec caracteres)]
    (apply str (repeatedly tamanho #(rand-nth caracteres-list)))))

(println (gerar-senha 12))